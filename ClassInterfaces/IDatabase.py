from abc import ABC, abstractmethod
from typing import Optional


class IDatabase(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def add_chunks(self, documents: list[str]) -> None: #change type T to class that represents LLM processed chunks
        pass

    @abstractmethod
    def get_documents(self, queries:list[str], documents_amount:Optional[int]) -> list[str]:
        pass