from PIL.PdfParser import PdfParser

from Parsers.LlamaParse import LlamaParseMd
from Tools.config import get_config
from LLMs.GoogleGemini import Gemini
from Tools.RAGPipline import RagPipline
from Chunkers.SymbolChunker import SymbolChunker
from Parsers.PdfPlumber import PdfPlumber
from Parsers.PyMuPdf4LLM import PyMuPdf4LLM
from Parsers.PyMuPdfRaw import PyMuPdfRaw

from DBs.ChromaDB import ChromaDB

if __name__ == "__main__":
    # Load configuration
    config = get_config()

    file_names = ["TestFiles/Monopoly.pdf"]
    questions = [
    "What are the denominations and quantities of the £1,500 given to each player?",
    "How much money does a player collect if they pass 'GO' and then draw a Chance card to 'Advance to GO' in one turn?",
    "What happens to an unowned Station if a player declines to buy it, and who can bid?",
    "Can a player collect double rent on an unmortgaged Site in a fully owned colour-group if another Site in that group is mortgaged?",
    "What rent is paid on a Utility owned by a player with both Utilities if the dice roll is 7?",
    "Can a player in Jail collect rent on an unmortgaged Property?",
    "How much does the Bank pay for a Hotel sold back, including the value of the exchanged Houses?",
    "In the Short Game, what must players do immediately after receiving two Title Deeds?",
    "What must a player do with Houses on a colour-group before selling one of its Sites?",
    "How is a mortgaged Property valued in the Time Limit Game’s final wealth calculation?"
]

    rag_client = RagPipline(LlamaParseMd(config), SymbolChunker, ChromaDB, Gemini(config["gemini_config"]), file_names, questions)
    answers = rag_client.process()
    print("\n\n".join(answers))

    # parser = LlamaParser(config["llama_parse"])
    # parser.open(file_names[0])
    #
    # while True:
    #     next_block = parser.get_next_text_block()
    #     if next_block is None:
    #         break
    #     print(next_block)
