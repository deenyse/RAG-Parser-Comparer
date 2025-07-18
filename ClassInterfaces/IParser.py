from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Iterator

class IParser(ABC):
    """
    Interface to module parsers system
    """
    def __init__(self, file_name:Optional[str] = None) -> None:
        self.file_name = file_name

    @abstractmethod
    def open(self, file_name:Optional[str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_next_text_block(self) -> Optional[str]:
        pass