from abc import ABC, abstractmethod
from typing import Optional, Any


class IDatabase(ABC):
    """
    Abstract base class for a vector database with a default embedding model included.
    Provides interface for adding and retrieving document chunks.
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add_chunks(self, collection: Any, documents: list[str]) -> None:
        """
        Add a list of document chunks to the database.
        Args:
            :param documents: (list[str]) List of text chunks to add.
            :param collection:
                Any DB collection to put documents into.
        """
        pass

    @abstractmethod
    def get_documents(self, collection:Any, queries:list[str], documents_amount:Optional[int]) -> list[str]:
        """
        Retrieve relevant documents from the database based on queries.
        Args:
            :param queries: (list[str]) List of search queries.
            :param documents_amount: (Optional[int]) Max number of documents to return.
            :param collection: collection to retrieve documents from.
        Returns:
            list[str]: List of retrieved document chunks.

        """
        pass

    @abstractmethod
    def create_collection(self, collection_name:str) -> Any:
        """
        Clears the database collection.
        """
        pass

    @abstractmethod
    def delete_collection(self, collection:Any) -> None:
        """
        Clears the database collection.
        """
        pass