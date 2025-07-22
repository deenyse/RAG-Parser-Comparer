from abc import ABC, abstractmethod
from typing import List, Union, Optional

class ILLM(ABC):
    def __init__(self, gemini_conf:dict) -> None:
        pass
    @abstractmethod
    def get_retrieval_embeddings_for_list_of_chunks(self, chunks:list[str]) -> list[str]: #need to change-> list[str] to returning type of Embeddings
        pass


    @abstractmethod
    def get_query_embeddings_for_list_of_chunks(self, chunks:list[str]) -> list[str]: #need to change-> list[str] to returning type of Embeddings
        pass

    @abstractmethod
    def get_response_based_on_context(self, queries:Union[List[str], str], model:Optional[str] = None, context:Optional[list[str]] = None) -> list[str]:
        pass

