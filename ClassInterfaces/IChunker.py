from abc import ABC, abstractmethod
from typing import  Iterator

class IChunker(ABC):
    def __init__(self) -> None:
       pass

    @abstractmethod
    def open(self, file_path:str) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_next_chunk(self) -> str or None:
        pass

    def __enter__(self) -> "IChunker":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
    def __iter__(self) -> Iterator[str]:
        while True:
            chunk = self.get_next_text_block()
            if chunk is None:
                break
            yield chunk