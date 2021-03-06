import Parser as p, CodeWriter as cw, os, sys

def main(dir):
    vmt = VMTranslator(dir)
    vmt.translate()

class VMTranslator:

    def __init__(self, dir):
        self.dir = dir
        self.code = cw.CodeWriter()

    def translate(self):
        for file in [f for f in os.listdir(self.dir) if f.endswith('.vm')]:
            filepath = os.path.join(self.dir, file)
            parser = p.Parser(filepath)
            parser.readFile()
            filestub = file.replace(".vm", "")

            for line in parser.lines:
                type = parser.type(line)
                arg1 = parser.arg1(line)
                arg2 = parser.arg2(line)
                self.code.writeComment(line)
                if type == "ARITHMETIC":
                    self.code.writeArithmetic(arg1)
                elif type == "PUSH":
                    self.code.writePush(arg1, arg2, filestub)
                elif type == "POP":
                    self.code.writePop(arg1, arg2, filestub)

        self.writeFile()

    def writeFile(self):
        outfile = self.dir + "\\" + self.dir.split("\\")[-1] + ".asm"
        with open(outfile, "w") as f:
            for line in self.code.out:
                f.write(line + "\n")

if __name__ == '__main__':
    main(sys.argv[1])
