# RAG Pipeline module: provides a universal function for running Retrieval-Augmented Generation (RAG) with pluggable parser, chunker, database, and LLM components.
from src.interfaces import IChunker
from src.interfaces.IDatabase import IDatabase
from src.interfaces.IParser import IParser
from src.interfaces.ILLM import ILLM
from typing import List, Optional, Any
import time

class RagPipline:
    def __init__(self, parser: IParser, chunker: IChunker, database: IDatabase, llm_client: ILLM, file_name: str, queries: List[str]) -> None:
        self.parser = parser
        self.chunker = chunker
        self.database = database
        self.llm_client = llm_client
        self.file_name = file_name
        self.queries = queries

        self.chunk_size = 300
        self.chunk_overlap = 75
        self.related_chunks_amount = 3

        self.database_client = database
        self.db_collection_name = f"{self.parser.info.name}-{self.file_name}-{self.chunker.name}".replace("/","")
        self.db_collection:Any = None

    def process(self) -> Optional[List[str]]:

        self.db_collection = self.database_client.create_collection(self.db_collection_name)
        print("DEBUG_PIPLINE: Created collection: " + self.db_collection.name)

        print("PIPLINE: Chopping and vectorizing files")
        start_vectorization = time.perf_counter()

        chunker_client = self.chunker(self.parser, self.file_name, self.chunk_size, self.chunk_overlap)

        with chunker_client as chunks:
            batch = []
            for chunk in chunks:
                batch.append(chunk)
                # Optional: add in batches to save memory if files are huge
                if len(batch) >= 20:
                    self.database_client.add_chunks(self.db_collection,batch)
                    batch = []


            if batch:
                self.database_client.add_chunks(self.db_collection,batch)

        end_vectorization = time.perf_counter()
        vectorization_time = end_vectorization - start_vectorization
        print(f"DONE: Vectorization took {vectorization_time:.2f} seconds.")


        print("PIPLINE: Retrieving related chunks")
        start_retrieval = time.perf_counter()

        context = self.database_client.get_documents(self.db_collection, self.queries, self.related_chunks_amount * len(self.queries))
        self.database_client.delete_collection(self.db_collection_name)

        end_retrieval = time.perf_counter()
        retrieval_time = end_retrieval - start_retrieval
        print(f"DONE: Retrieval took {retrieval_time:.4f} seconds.")

        print("PIPLINE: Generating response...")
        start_generation = time.perf_counter()

        response = self.llm_client.get_response_based_on_context(self.queries, context=context)

        end_generation = time.perf_counter()
        generation_time = end_generation - start_generation
        print(f"DONE: Generation took {generation_time:.2f} seconds.")

        total_time = vectorization_time + retrieval_time + generation_time
        print(f"\n--- Total Pipeline Execution Time: {total_time:.2f} seconds ---")

        return response