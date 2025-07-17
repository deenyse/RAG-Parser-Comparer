from Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.SymbolChunker import Chunker

if __name__ == "__main__":
    '''
    "TestFiles/ParserTestingPDF.pdf"
    '''


    chunker = Chunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 10, 2)
    chunker.open()
    print(chunker.get_next_chunk())
    print("--------------")
    print(chunker.get_next_chunk())
    print("--------------")
    print(chunker.get_next_chunk())
    print("--------------")
    print(chunker.get_next_chunk())


    # #WORKS
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    #
    # print(next(iter(parser)))

    # #WORKS _2_

    # with ParsByPdfPlumber("TestFiles/ParserTestingPDF.pdf") as parser:
    #     for chunk in parser:
    #         print(chunk)
