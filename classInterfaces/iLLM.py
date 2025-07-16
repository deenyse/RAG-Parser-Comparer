from abc import ABC, abstractclassmethod



class iLLM(ABC):
    def __init__(self, apiKey) -> None:
        pass

    @abstractclassmethod
    def getRetrievalEmbeddingsForListOfChunks(self, chunks:list[str]) -> list[str]: #need to change-> list[str] to returning type of Embeddings
        pass


    @abstractclassmethod
    def getQueryEmbeddingsForListOfChunks(self, chunks:list[str]) -> list[str]: #need to change-> list[str] to returning type of Embeddings
        pass

    @abstractclassmethod
    def getResponceBasedOnContext(self, context:list[str], queries:list[str] ) -> list[str]:
        pass

