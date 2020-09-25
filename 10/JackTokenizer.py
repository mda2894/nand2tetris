class JackTokenizer:

    def __init__(self, file):
        self.file = file
        self.tokens = []

    def readFile(self):
        with open(self.file) as f:
            self.lines = f.read().splitlines()

        self.lines = [line.split("//", 1)[0].strip() for line in self.lines]
        self.lines = [line for line in self.lines if line]

    def tokenize(self):
        for line in self.lines:
            for char in line:
