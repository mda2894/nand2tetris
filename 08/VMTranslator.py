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
            self.file = self.path
            self.translateFile()
        else:
            self.dir = self.path
            self.translateDir()

    def translateFile(self):
        parser = p.Parser(self.file)
        parser.readFile()
        fileStub = self.file.replace(".vm", "")

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

        self.writeFile()

    def translateDir(self):
        self.code.writeInit()

        fileList = [f for f in os.listdir(self.dir) if f.endswith('.vm')]

        for file in fileList:
            filePath = os.path.join(self.dir, file)
            parser = p.Parser(filePath)
            parser.readFile()
            fileStub = file.replace(".vm", "")

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

        self.writeFile()

    def writeFile(self):
        if self.isFile:
            outfile = self.file.replace(".vm", ".asm")
        else:
            outfile = os.path.split(self.dir)[1] + ".asm"
            outfile = os.path.join(self.dir, outfile)
        with open(outfile, "w") as f:
            for line in self.code.out:
                f.write(line + "\n")

if __name__ == '__main__':
    main(sys.argv[1])
