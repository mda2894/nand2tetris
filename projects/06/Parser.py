class Parser:

    def __init__(self, file):
        self.file = file

    def readFile(self):
        with open(self.file) as f:
            self.lines = f.read().splitlines()

        self.lines = [line.split("//", 1)[0].strip() for line in self.lines]
        self.lines = [line for line in self.lines if line]

    def type(self, line):
        if line.startswith("("):
            return "L"
        elif line.startswith("@"):
            return "A"
        else:
            return "C"

    def symb(self, line):
        if self.type(line) == "L":
            return line[1:-1]
        elif self.type(line) == "A":
            return line[1:]
        else:
            return None

    def dest(self, line):
        if self.type(line) == "C":
            if "=" in line:
                return line.partition("=")[0]
            else:
                return ""
        else:
            return None

    def jump(self, line):
        if self.type(line) == "C":
            if ";" in line:
                return line.partition(";")[2]
            else:
                return ""
        else:
            return None

    def comp(self, line):
        if self.type(line) == "C":
            if "=" in line and ";" in line:
                parts = line.partition("=")
                return parts[2].partition(";")[0]
            elif "=" in line:
                return line.partition("=")[2]
            elif ";" in line:
                return line.partition(";")[0]
            else:
                return line
        else:
            return None
