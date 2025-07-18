from Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.SymbolChunker import SymbolChunker

if __name__ == "__main__":
# TODO simplify parser structure, to remove redundant context manager construction
#   move this construction into IChunker, so i can open Chunkers as a context(in the RAG pipline)



    # with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
    #     for block in chunker:
    #         print(block)
    #         print("--------")

    chunker = SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70)
    chunker.open()

    with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
        for chunk in chunker:
            print(chunk)

    # #WORKS
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    #
    # print(next(iter(parser)))

    # #WORKS _2_

    # with ParsByPdfPlumber("TestFiles/ParserTestingPDF.pdf") as parser:
    #     for chunk in parser:
    #         print(chunk)
