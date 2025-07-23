from abc import ABC, abstractmethod
from typing import List, Union, Optional

class ILLM(ABC):
    def __init__(self, gemini_conf:dict) -> None:
        pass

    @abstractmethod
    def get_response_based_on_context(self, queries:Union[List[str], str], context:Optional[list[str]] = None, model:Optional[str] = None ) -> Optional[list[str]]:
        pass

