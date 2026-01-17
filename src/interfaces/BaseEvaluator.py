from dataclasses import dataclass
from typing import List, Optional, Any
from abc import ABC, abstractmethod


@dataclass
class EvalContext:
    question: str
    rag_answer: str
    ground_truth: str
    chunks: List[str]


class BaseEvaluator(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Test Name"""
        pass

    @abstractmethod
    def evaluate(self, ctx: EvalContext) -> dict:
        """Method to evaluate a question"""
        pass