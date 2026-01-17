from src.interfaces.BaseEvaluator import BaseEvaluator, EvalContext
from src.interfaces.BaseLlm import BaseLLM

"""
Evaluates by LLM
OUT:
    number: point based evaluation.
        Gives score from 0 to 100

    category: Categorizing RAG answer to groups
            Correct, Partially correct, Wrong

"""

class LlmCorrectnessEvaluator(BaseEvaluator):
    name = "LlmCorrectnessEvaluator"

    def  __init__(self, llm:BaseLLM):
        self.llm = llm

    def evaluate(self, ctx: EvalContext) -> int:
        prompt = f"""
        You are an automated evaluator of a Retrieval-Augmented Generation (RAG) system.

        Your task is to evaluate how well the RAG answer matches the ground truth.
        You MUST base your evaluation strictly on the provided ground truth.
        Do NOT use any external knowledge or assumptions.

        <evaluation_context>
        Question:
        {ctx.question}

        RAG Answer:
        {ctx.rag_answer}

        Ground Truth:
        {ctx.ground_truth}
        </evaluation_context>

        Evaluation rules:
        - Score the RAG answer with a SINGLE INTEGER from 0 to 100.
        - 100 means the RAG answer is fully correct, complete, and directly answers the question.
        - 0 means the RAG answer is completely incorrect, irrelevant, or contradicts the ground truth.
        - Partial correctness or missing details should result in a proportional score.

        """

        return self.llm.get_int_response(prompt)