from abc import ABC, abstractmethod
from typing import  Iterator, Optional

from src.interfaces import IParser


class IChunker(ABC):
    """
    Abstract class for chunker classes.
    Takes:
        parser: IParser by which the file will be parsed
        file_name: name of the file to be parsed
        chunk_size: size of the chunk
        overlap_size: size of the previous chunk, that will be added to next one
    """
    def __init__(self, parser: IParser, file_name:str, chunk_size:int, overlap_size:int) -> None:
        self.file_name = file_name
        self.parser = parser
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

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