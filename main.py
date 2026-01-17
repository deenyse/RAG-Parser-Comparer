from src.evaluations.LlmCorrectnessEvaluator import LlmCorrectnessEvaluator
from src.modules.parsers.ParserFactory import ParserFactory
from src.piplenes.EvaluatingRAGPipline import EvaluatingRAGPiplineParams, EvaluatingRAGPipline
from src.utils.Config import Config
# from src.piplenes.RAGPipline import RagPipline
from src.modules.llms.GoogleGemini import Gemini
from src.modules.vector_dbs.ChromaDB import ChromaDB
from src.modules.chunkers.SymbolChunker import SymbolChunker, ChunkerParams
from src.utils.FileManager import FileManager
from src.utils.MongoDBHandler import MongoDBHandler
if __name__ == "__main__":
    model = Gemini(Config.get_value("gemini_config", "api_key"), Config.get_value("gemini_config", "query_model"))
    chunker_params = ChunkerParams(
        chunk_size=300,
        chunk_overlap=75
    )

    pipline_params = EvaluatingRAGPiplineParams(
        file_names= ["Monopoly.pdf"],
        parsers=[ParserFactory.pdf_plumber()],
        chunkers=[SymbolChunker(chunker_params)],
        vdb=ChromaDB(),
        chunks_amount=3,
        llm=model,
        evals=[LlmCorrectnessEvaluator(model)],
        mongo=MongoDBHandler(Config.get_value("mongodb", "uri"), Config.get_value("mongodb", "db_name")),
        fm= FileManager()
    )

    pipline = EvaluatingRAGPipline(pipline_params)
    pipline.process()



    # mongo = MongoDBHandler(Config.get_value("mongodb", "uri"), Config.get_value("mongodb", "db_name"))
    # answers = mongo.getFileAnswers("UNKyrgystan.PDF")
    #
    # print(len(answers))

    # file_name = "data/UNKyrgystan.PDF"
    # questions = mongo.getFileQuestions("UNKyrgystan.PDF")
    # rag_client = (
    #     RagPipline(ParserFactory.py_mu_pfd_4_llm(),
    #                SymbolChunker,
    #                ChromaDB(),
    #                Gemini(Config.get_value("gemini_config", "api_key"), Config.get_value("gemini_config", "query_model")),
    #                file_name,
    #                questions)
    # )
    # answers = rag_client.process()
    # print("\n\n".join(answers))

    #
    # fm = FileManager("data/files")
    # fm.reinitFiles()
    # fm.updateFiles(mongo)
    # print()