from abc import ABC, abstractclassmethod

class Chunk():
    pass

class IDatabase(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def addChunks(self, chunks: list[Chunk]) -> None: #change type T to class that represents LLM processed chunks
        pass

    @abstractclassmethod
    def getfDocuments (self, query_embedding, documents_amount) -> list[str]: #returns retrieved documents for context (func NEEDs some renaming)
        pass