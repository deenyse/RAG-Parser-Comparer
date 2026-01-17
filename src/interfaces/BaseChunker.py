from abc import ABC, abstractmethod
from typing import  Iterator, Optional
from dataclasses import dataclass

from src.interfaces.BaseParser import BaseParser

@dataclass
class ChunkerParams:
    chunk_size: int
    chunk_overlap: int

class BaseChunker(ABC):
    """
    Abstract class for chunker classes.
    Takes:
        parser: IParser by which the file will be parsed
        file_name: name of the file to be parsed
        chunk_size: size of the chunk
        overlap_size: size of the previous chunk, that will be added to next one
    """
    @property
    @abstractmethod
    def parser(self) -> Optional[BaseParser]:
        pass

    def __init__(self, params: ChunkerParams) -> None:
        if params.chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if params.chunk_overlap < 0:
            raise ValueError("overlap_size cannot be negative")
        if params.chunk_overlap > params.chunk_size:
            raise ValueError("overlap_size cannot be larger than chunk_size")
        self.params = params

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Chunker identification name
        """
        pass

    @abstractmethod
    def open(self, parser:BaseParser, file_name:str) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_next_chunk(self) -> Optional[str]:
        pass