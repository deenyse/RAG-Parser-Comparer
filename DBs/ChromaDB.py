from ClassInterfaces.IDatabase import IDatabase
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
        self.collection.add(
            ids=[str(uuid4()) for _ in range(len(documents))],
            documents=documents,
        )


    def get_documents(self, queries:list[str], documents_amount:Optional[int]) -> Optional[list[list[str]]]:
        result = self.collection.query(
            query_texts=queries,
            n_results=documents_amount,
        )

        return result["documents"]






