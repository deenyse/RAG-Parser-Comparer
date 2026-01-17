from dataclasses import dataclass
from traceback import print_tb
from typing import List

from sympy.physics.vector.printing import params

from src.interfaces.BaseChunker import BaseChunker
from src.interfaces.BaseEvaluator import BaseEvaluator, EvalContext
from src.interfaces.BaseVectorDB import BaseVectorDB
from src.interfaces.BaseParser import BaseParser
from src.interfaces.BaseLlm import BaseLLM
from src.utils.FileManager import FileManager
from src.utils.MongoDBHandler import MongoDBHandler


@dataclass
class EvaluatingRAGPiplineParams:
    file_names: List[str]
    parsers: List[BaseParser]
    chunkers: List[BaseChunker]
    vdb: BaseVectorDB
    chunks_amount:int
    llm: BaseLLM
    evals: List[BaseEvaluator]
    mongo: MongoDBHandler
    fm: FileManager


class EvaluatingRAGPipline:
    def __init__(self, params: EvaluatingRAGPiplineParams):
        self.params = params

        #TODO: fix only 1 chunker supported
        if len(params.chunkers) != 1:
            raise ValueError("Only one chunker allowed")


    def process(self) -> None:
        print("PIPLINE: Starting evaluating RAGPipline")

        for file_name in self.params.file_names:
            for parser in self.params.parsers:
                for chunker in self.params.chunkers:
                    for test in self.params.evals:
                        collection_name = f"{parser.info.name}-{file_name}-{chunker.name}"
                        self.params.vdb.create_collection(collection_name)
                        print("PIPLINE: Created collection: " + collection_name)
                        print("PIPLINE: Chopping and vectorizing files")

                        chunker.open(parser, self.params.fm.get_file_location(file_name))

                        batch = []
                        while True:
                            chunk = chunker.get_next_chunk()
                            if chunk is None:
                                break
                            batch.append(chunk)

                            if len(batch) >= 20:
                                self.params.vdb.add_chunks(collection_name, batch)
                                batch = []

                        if batch:
                            self.params.vdb.add_chunks(collection_name, batch)

                        print(f"PIPLINE: Vectorization finished")

                        print("PIPLINE: Retrieving related chunks")
                        """
                        TODO:
                        Loop through questions and do check 1 by 1 instead many questions at the same time many
                        """

                        questions = self.params.mongo.getFileQuestions(file_name)
                        context = self.params.vdb.get_documents(collection_name, questions, self.params.chunks_amount * len(questions))
                        self.params.vdb.delete_collection(collection_name)

                        print(f"PIPLINE: Retrieval done.")
                        print("PIPLINE: Generating response...")

                        response = self.params.llm.get_response_based_on_context(questions, context=context)

                        print(f"PIPLINE: Generation for test {collection_name} is done.")

                        print(f"PIPLINE: Getting question answers.")
                        g_truth = self.params.mongo.getFileAnswers(file_name)
                        print(g_truth)

                        print(f"PIPLINE: Started evaluation.")
                        eval_results = []
                        for (question, answer, gt) in zip(questions, response, g_truth):
                            eval_results.append(
                                test.evaluate(EvalContext(
                                question=question,
                                rag_answer=answer,
                                ground_truth=gt,
                                chunks=context
                                ))
                            )

                        print("PIPLINE: Evaluation done.")

                        for (question, answer, correct_answer, res) in zip(questions, response, g_truth, eval_results):
                            print(f"q: {question}\na: {answer}\ng: {correct_answer}\nres: {res}")
                """
                TODO:
                HERE IS REQUIRED NOT TO REPARSE FILE, BUT MOOVE TO FILE START POSITION
                    need to update BaseParser and implement this feature in all parsers
                """