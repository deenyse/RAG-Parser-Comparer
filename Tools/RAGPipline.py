# RAG Pipeline module: provides a universal function for running Retrieval-Augmented Generation (RAG) with pluggable parser, chunker, database, and LLM components.
from uvicorn import Config
from ClassInterfaces import IParser, IChunker, IDatabase
from ClassInterfaces.ILLM import ILLM
from typing import List, Union, Type, Optional

class RagPipline:
    def __init__(self, parser: IParser, chunker: IChunker, database: IDatabase, llm: Union[Type[ILLM], ILLM], config: dict,
                files_names: List[str], queries: List[str]) -> None:
        self.parser = parser
        self.chunker = chunker
        self.database = database
        self.llm = llm
        self.config = config
        self.files_names = files_names
        self.queries = queries

        self.chunk_size = 200
        self.chunk_overlap = 50
        self.related_chunks_amount = 10

        self.llm_client = llm(config)
        self.database_client = database()

    def process(self) -> Optional[List[str]]:

        for file_name in self.files_names:
            chunker_client = self.chunker(self.parser, file_name, self.chunk_size, self.chunk_overlap)
            with chunker_client  as chunks:
                for chunk in chunks:
                    self.database_client.add_chunks([chunk])

        context = self.database_client.get_documents(self.queries, self.related_chunks_amount)



        response = self.llm_client.get_response_based_on_context(self.queries, context=context)
        return response