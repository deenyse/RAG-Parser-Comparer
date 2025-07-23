from abc import ABC, abstractmethod
from typing import Optional


class IDatabase(ABC):
    """
    Abstract base class for a vector database with a default embedding model included.
    Provides interface for adding and retrieving document chunks.
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add_chunks(self, documents: list[str]) -> None:
        """
        Add a list of document chunks to the database.
        Args:
            documents (list[str]): List of text chunks to add.
        """
        pass

    @abstractmethod
    def get_documents(self, queries:list[str], documents_amount:Optional[int]) -> list[str]:
        """
        Retrieve relevant documents from the database based on queries.
        Args:
            queries (list[str]): List of search queries.
            documents_amount (Optional[int]): Max number of documents to return.
        Returns:
            list[str]: List of retrieved document chunks.
        """
        pass