# RAG Pipeline module: provides a universal function for running Retrieval-Augmented Generation (RAG) with pluggable parser, chunker, database, and LLM components.
from ClassInterfaces import IParser, IChunker, IDatabase
from ClassInterfaces.ILLM import ILLM
from typing import List, Union, Type, Optional


def rag_pipline(parser: IParser, chunker: IChunker, database: IDatabase, llm: Union[Type[ILLM], ILLM], config: dict,
                file_name: str, queries: List[str]) -> Optional[List[str]]:
    """
    Universal RAG pipeline that works with any LLM implementing the ILLM interface.

    Args:
        parser (IParser): Parser for file processing.
        chunker (IChunker): Chunker for splitting text into parts.
        database (IDatabase): Database for storing and searching chunks.
        llm (Union[Type[ILLM], ILLM]): Class or instance of LLM implementing ILLM.
        config (dict): Configuration for initializing LLM (if a class is passed).
        file_name (str): Path to the file to process.
        queries (List[str]): List of queries for searching and generating responses.

    Returns:
        List[str]: List of responses from LLM.

    Raises:
        ValueError: If the llm type is incorrect or an error occurs in the pipeline.
    """
    test_llm = llm(config)
    test_chunker = chunker(parser, file_name, 400, 100)
    test_database = database()

    with test_chunker as chunks:
        for chunk in chunks:
            test_database.add_chunks([chunk])

    context = test_database.get_documents(queries, 20)



    response = test_llm.get_response_based_on_context(queries, context=context)
    return response

