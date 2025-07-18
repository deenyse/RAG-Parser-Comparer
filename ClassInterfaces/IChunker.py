from abc import ABC, abstractmethod
from typing import  Iterator, Optional

class IChunker(ABC):
    def __init__(self, file_name:str) -> None:
       self.file_name = file_name

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_next_chunk(self) -> Optional[str]:
        pass

    def __enter__(self) -> "IChunker":
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def __iter__(self) -> Iterator[str]:
        while True:
            chunk = self.get_next_chunk()
            if chunk is None:
                break
            yield chunk