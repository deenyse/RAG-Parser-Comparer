from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Iterator

class IParser(ABC):
    """
    Abstract base class for file parsers in the system.
    Provides interface for opening, closing, and iterating over text blocks in a file.
    """
    def __init__(self, file_name:Optional[str] = None, config:Optional[dict] = None) -> None:
        """
        Initialize the parser with an optional file name.
        Args:
            file_name (Optional[str]): File to parse.
        """
        self.file_name = file_name

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