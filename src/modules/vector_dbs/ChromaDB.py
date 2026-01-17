from src.interfaces.BaseVectorDB import BaseVectorDB
import chromadb
from chromadb.types import Collection
from uuid import uuid4
from typing import Optional, Any


class ChromaDB(BaseVectorDB):
    chroma_client = None

    def __init__(self) -> None:
        super().__init__()
        self.chroma_client = chromadb.Client()

    def add_chunks(self, collection_name: str, documents: list[str]) -> None:
        if not documents:
            return
        collection = self.chroma_client.get_collection(collection_name)

        collection.add(
            ids=[str(uuid4()) for _ in range(len(documents))],
            documents=documents,
        )


    def get_documents(self, collection_name: str,queries:list[str], documents_amount:Optional[int]) -> Optional[list[str]]:
        collection = self.chroma_client.get_collection(collection_name)
        result = collection.query(
            query_texts=queries,
            n_results=documents_amount,
        )

        # ChromaDB return list[list[str]]. Must change it into list[str]
        raw_docs = result["documents"]
        unique_docs = set()

        for sublist in raw_docs:
            for doc in sublist:
                unique_docs.add(doc)

        return list(unique_docs)

    def delete_collection(self, collection_name: str) -> None:
        collection = self.chroma_client.get_collection(collection_name)
        try:
            collection.delete()
        except Exception:
            pass  # Collection might not exist

    def create_collection(self, collection_name:str) -> None:
        # self.collection = self.chroma_client.create_collection(name="RetrieveCollection")
        return self.chroma_client.create_collection(name=collection_name)





