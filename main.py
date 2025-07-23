from Tools.config import get_config
from LLMs.GoogleGemini import Gemini
from Tools.RAGPipline import rag_pipline
from Chunkers.SymbolChunker import SymbolChunker
from Parsers.PdfPlumber import ParsByPdfPlumber
from DBs.ChromaDB import ChromaDB

if __name__ == "__main__":
    # Load configuration
    config = get_config()

    print(config)
    file_name = "TestFiles/biography-cz.pdf"
    questions = [
    "Jak se jmenuje osoba, jejíž životopis je popsán v dokumentu?",
    "When and where was Ivan Petrov born?",
    "Jaké vzdělání získal Ivan Petrov?",
    "In which year did Ivan found the company «TechnoSparks»?",
    "Jakou pozici zastává Ivan ve společnosti «FutureTech»?",
    "What is the name of the foundation established by Ivan, and what is its purpose?",
    "Kolik studentů podpořila nadace «Vědomosti pro budoucnost»?",
    "What is the name of Ivan’s wife and what is her profession?",
    "Jaká ocenění získal Ivan Petrov?",
    "What is Ivan’s hobby related to music?",
    "Na jakém projektu Ivan v současnosti pracuje?",
    "What is Ivan’s long-term dream in the field of education?",
    "Kolik dětí má Ivan a jak se jmenují?",
    "In which year was the company «TechnoSparks» acquired by an international corporation?",
    "Jaký balet je Ivanovým oblíbeným dílem?"
]
    answers = rag_pipline(ParsByPdfPlumber, SymbolChunker, ChromaDB, Gemini, config["gemini_config"], file_name, questions)

    print("\n\n".join(answers))

#TODO:
# ----------FUTURE_PLANS----------
# 2. Write some comments to RAG pipline, Gemini, iDatabase(ChromaDB),
# 4. Update README
# 5. Maby change RAG pipline to Class instead of function(assume yes - because i have a lot of params that will be needed to interchange[like file location, etc.]
#   a. Need to think through Parsers Testing Module
# 6. Implement further parsers.
# 7. Check how systems are interchangeable(i mean parsers, DBs, LLMs, etc.)
# ----------STRUCTURE_SIMPLIFICATION----------
# 3. Do i really need all those chunkers(i assume yes, because the way i treat context can influence output)
