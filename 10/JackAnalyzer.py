import JackTokenizer as jt, CompilationEngine as ce, os, sys

def main(path):
    analyzer = JackAnalyzer(path)
    analyzer.analyze()

class JackAnalyzer:

    def __init__(self, path):
        self.path = path

    def analyze(self):
        self.isFile = os.path.isfile(self.path)
        if self.isFile:
            self.analyzeFile(self.path)
        else:
            self.analyzeDir(self.path)

    def analyzeDir(self, dir):
        fileList = [f for f in os.listdir(dir) if f.endswith('.jack')]

        for file in fileList:
            filePath = os.path.join(dir, file)
            self.analyzeFile(filePath)

    def analyzeFile(self, file):
        token = jt.JackTokenizer(file)
        token.tokenize()
        token.writeTokens()
