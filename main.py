from Parsers.PdfPlumber import ParsByPdfPlumber


if __name__ == "__main__":
    # print("Hello World")

    #Way to open _1_
    with ParsByPdfPlumber() as parser:
        parser.open("TestFiles/ParserTestingPDF.pdf")
        for chunk in parser:
            print(chunk)

    # #Way to open _2_
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    # for chunk in parser:
    #     print(chunk)

    # #Way to open _3_
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    # while True:
    #     text = parser.get_next_text_block()
    #     if text is None:
    #         break
    #     print(text)