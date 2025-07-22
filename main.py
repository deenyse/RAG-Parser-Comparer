from Tools.config import get_config
from Tools.LLMs.GoogleGemini import Gemini
from Tools.RAGPipline import rag_pipline
from Tools.Chunkers.SymbolChunker import SymbolChunker
from Tools.Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.DBs.ChromaDB import ChromaDB

if __name__ == "__main__":
    config = get_config()
    answers = rag_pipline(ParsByPdfPlumber, SymbolChunker, ChromaDB, Gemini, config["gemini_config"], "TestFiles/Monopoly.pdf", ["What this file is about", "What is Bankruptcy?", "What is name of this game?", "Как я могу что-то купить?"])

    # llm = Gemini(config["gemini_config"])
    # answers = llm.get_response_based_on_context(["how old am i", "am i male"], context=["im 21 yo male"])
    print("\n\n".join(answers))

#TODO:
# ----------FUTURE_PLANS----------
# 1. In case of error Gemini could return None. Need to change rag_pipline output to Optional
# 2. Write some comments to RAG pipline, Gemini, iDatabase(ChromaDB),
# 3. Config is not loading from echo $GEMINI_API_KEY (environmental variables)
# 4. Update README
# 5. Maby change RAG pipline to Class instead of function
#   a. Need to think through Parsers Testing Module
# 6. Implement further parsers.
# 7. Check how systems are interchangeable(i mean parsers, DBs, LLMs, etc.)
# ----------STRUCTURE_SIMPLIFICATION----------
# 1. Maby i need to rethink folder tree(i have almost everything in Tools folder
# 2. Perhaps i need delete LLM embeddings functions
# 3. Do i really need all those chunkers(i assume yes, because the way i treat context can influence output)
