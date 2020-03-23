class Parser:

    def __init__(self, file):
        self.file = file
        self.typeTable = {
            "push" : "PUSH",
            "pop" : "POP",
            "label" : "LABEL",
            "goto" : "GOTO",
            "if-goto" : "IF",
            "function" : "FUNCTION",
            "call" : "CALL",
            "return" : "RETURN"
        }

    def readFile(self):
        with open(self.file) as f:
            self.lines = f.read().splitlines()

        self.lines = [line.split("//", 1)[0].strip() for line in self.lines]
        self.lines = [line for line in self.lines if line]

    def type(self, line):
        start = line.split()[0]
        return self.typeTable.get(start, "ARITHMETIC")

    def arg1(self, line):
        type = self.type(line)
        if type == "ARITHMETIC":
            return line.split()[0]
        elif type == "RETURN":
            return None
        else:
            return line.split()[1]

    def arg2(self, line):
        type = self.type(line)
        if type in ["PUSH", "POP", "FUNCTION", "CALL"]:
            return line.split()[2]
        else:
            return None
