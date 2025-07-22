from Tools.config import get_config
from Tools.LLMs.GoogleGemini import Gemini
from Tools.RAGPipline import rag_pipline
from Tools.Chunkers.SymbolChunker import SymbolChunker
from Tools.Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.DBs.ChromaDB import ChromaDB

if __name__ == "__main__":
    config = get_config()
    answers = rag_pipline(ParsByPdfPlumber, SymbolChunker, ChromaDB, Gemini, config["gemini_config"], "TestFiles/Monopoly.pdf", ["What this file is about", "What is Bankruptcy?", "What is name of this game?"])

    # llm = Gemini(config["gemini_config"])
    # answers = llm.get_response_based_on_context(["how old am i", "am i male"], context=["im 21 yo male"])
    print("\n\n".join(answers))

