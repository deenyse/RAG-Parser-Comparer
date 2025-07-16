from classInterfaces.iParser import iParser


class Parser(iParser):
    def __init__(self, name):
        super().__init__(name)


    def parse(self):
        print(self.name)

if __name__ == "__main__":
    myParser = Parser("MyParser")
    myParser.parse()