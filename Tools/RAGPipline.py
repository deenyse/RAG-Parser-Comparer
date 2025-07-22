from ClassInterfaces import IParser, IChunker, IDatabase
from ClassInterfaces.ILLM import ILLM
from typing import List, Union, Type


def rag_pipline(parser: IParser, chunker: IChunker, database: IDatabase, llm: Union[Type[ILLM], ILLM], config: dict,
                file_name: str, queries: List[str]) -> List[str]:
    """
    Универсальный RAG-конвейер, работающий с любой LLM, реализующей интерфейс ILLM.

    Args:
        parser (IParser): Парсер для обработки файла.
        chunker (IChunker): Чанкер для разделения текста на части.
        database (IDatabase): База данных для хранения и поиска чанков.
        llm (Union[Type[ILLM], ILLM]): Класс или экземпляр LLM, реализующий ILLM.
        config (dict): Конфигурация для инициализации LLM (если передан класс).
        file_name (str): Путь к файлу для обработки.
        queries (List[str]): Список запросов для поиска и генерации ответов.

    Returns:
        List[str]: Список ответов от LLM.

    Raises:
        ValueError: Если передан неверный тип llm или произошла ошибка в конвейере.
    """
    test_llm = llm(config)
    test_chunker = chunker(parser, file_name, 400, 100)
    test_database = database()

    with test_chunker as chunks:
        for chunk in chunks:
            test_database.add_chunks([chunk])

    context = test_database.get_documents(queries, 10)



    response = test_llm.get_response_based_on_context(queries, context=context)
    return response

