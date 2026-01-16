from src.interfaces.IDatabase import IDatabase
import chromadb
from uuid import uuid4
from typing import Optional

class ChromaDB(IDatabase):
    chroma_client = None
    collection = None
    def __init__(self) -> None:
        super().__init__()
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(name="RetrieveCollection")

    def add_chunks(self, documents: list[str]) -> None:
        if not documents:
            return

        self.collection.add(
            ids=[str(uuid4()) for _ in range(len(documents))],
            documents=documents,
        )


    def get_documents(self, queries:list[str], documents_amount:Optional[int]) -> Optional[list[str]]:
        result = self.collection.query(
            query_texts=queries,
            n_results=documents_amount,
        )

        # ChromaDB return list[list[str]]. Нам нужно превратить это в list[str]
        raw_docs = result["documents"]
        unique_docs = set()

        for sublist in raw_docs:
            for doc in sublist:
                unique_docs.add(doc)

        return list(unique_docs)

    def reset(self) -> None:
        try:
            self.chroma_client.delete_collection("RetrieveCollection")
        except Exception:
            pass  # Collection might not exist
        self.collection = self.chroma_client.create_collection(name="RetrieveCollection")






