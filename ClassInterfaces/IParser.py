from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Iterator

class IParser(ABC):

    def __init__(self, file_name:Optional[str] = None) -> None:
        self.file_name = file_name


    @abstractmethod
    def open(self, file_name:Optional[str] = None) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_next_text_block(self) -> Optional[str]:
        pass

    def __enter__(self) -> "IParser":
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
    def __iter__(self) -> Iterator[str]:
        while True:
            chunk = self.get_next_text_block()
            if chunk is None:
                break
            yield chunk