import Parser as p, CodeWriter as cw, os, sys

def main(path):
    vmt = VMTranslator(path)
    vmt.translate()

class VMTranslator:

    def __init__(self, path):
        self.path = path
        self.code = cw.CodeWriter()

    def translate(self):
        self.isFile = os.path.isfile(self.path)
        if self.isFile:
            self.translateFile(self.path)
            self.writeFile()
        else:
            self.translateDir(self.path)
            self.writeFile()

    def translateDir(self, dir):
        self.code.writeInit()

        fileList = [f for f in os.listdir(dir) if f.endswith('.vm')]

        for file in fileList:
            filePath = os.path.join(dir, file)
            self.translateFile(filePath)

    def translateFile(self, file):
        parser = p.Parser(file)
        parser.readFile()
        fileStub = os.path.split(file)[1].replace(".vm", "")

        for line in parser.lines:
            type = parser.type(line)
            arg1 = parser.arg1(line)
            arg2 = parser.arg2(line)
            self.code.writeComment(line)

            if type == "ARITHMETIC":
                self.code.writeArithmetic(arg1)
            elif type == "PUSH":
                self.code.writePush(arg1, arg2, fileStub)
            elif type == "POP":
                self.code.writePop(arg1, arg2, fileStub)
            elif type == "LABEL":
                self.code.writeLabel(arg1)
            elif type == "GOTO":
                self.code.writeGoto(arg1)
            elif type == "IFGOTO":
                self.code.writeIfGoto(arg1)
            elif type == "FUNCTION":
                self.code.writeFunction(arg1, arg2)
            elif type == "CALL":
                self.code.writeCall(arg1, arg2)
            elif type == "RETURN":
                self.code.writeReturn()

    def writeFile(self):
        if self.isFile:
            outfile = self.path.replace(".vm", ".asm")
        else:
            outfile = os.path.split(self.path)[1] + ".asm"
            outfile = os.path.join(self.path, outfile)
        with open(outfile, "w") as f:
            for line in self.code.out:
                f.write(line + "\n")

if __name__ == '__main__':
    main(sys.argv[1])
