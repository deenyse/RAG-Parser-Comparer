from abc import ABC, abstractmethod
from typing import Optional, Iterator

from src.interfaces.parser import ParserInfo


class IParser(ABC):
    """
    Abstract base class for file parsers in the system.
    Provides interface for opening, closing, and iterating over text blocks in a file.
    """

    @property
    @abstractmethod
    def info(self) -> ParserInfo:
        """
        Parser Metadata
        """
        pass
    @abstractmethod
    def open(self, file_name:Optional[str]) -> None:
        """
        Open the file for parsing.
        Args:
            file_name (Optional[str]): File to open.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Close the file and release resources.
        """
        pass

    @abstractmethod
    def get_next_text_block(self) -> Optional[str]:
        """
        Get the next block of text from the file.
        Returns:
            Optional[str]: The next text block, or None if end of file.
        """
        pass