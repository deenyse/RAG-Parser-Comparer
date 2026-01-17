from enum import Enum, auto
from dataclasses import dataclass

class FileType(Enum):
    PDF = auto()
    DOCX = auto()

class Connectivity(Enum):
    ONLINE = auto()
    OFFLINE = auto()

@dataclass(frozen=True)
class ParserInfo:
    supported_types: list[FileType]
    connectivity: Connectivity
    is_ocr: bool
