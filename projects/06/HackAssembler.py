import Parser as p, Code as c, SymbolTable as s, sys

def main(file):
    asm = Assembler(file)
    asm.assemble()

class Assembler:

    def __init__(self, file):
        self.file = file
        self.parser = p.Parser(self.file)
        self.code = c.Code()
        self.symb = s.SymbolTable()

    def assemble(self):
        self.pass1()
        self.pass2()
        self.writeFile()

    def pass1(self):
        self.parser.readFile()
        linenum = 0

        for line in self.parser.lines:
            command = self.parser.type(line)
            if command == "L":
                self.symb.addEntry(self.parser.symb(line), linenum)
            else:
                linenum += 1

    def pass2(self):
        out = list()
        varnum = 16

        for line in self.parser.lines:
            command = self.parser.type(line)

            if command == "A":
                symb = self.parser.symb(line)

                if symb.isdigit():
                    out.append(self.code.address(symb))
                elif self.symb.contains(symb):
                    out.append(self.code.address(self.symb.getAddress(symb)))
                else:
                    self.symb.addEntry(symb, varnum)
                    varnum += 1
                    out.append(self.code.address(self.symb.getAddress(symb)))

            elif command == "C":
                dest = self.code.dest(self.parser.dest(line))
                comp = self.code.comp(self.parser.comp(line))
                jump = self.code.jump(self.parser.jump(line))
                out.append("111" + comp + dest + jump)

        self.out = out

    def writeFile(self):
        outfile = self.file.replace(".asm", ".hack")
        with open(outfile, "w") as f:
            for line in self.out:
                f.write(line + "\n")

def test():
    file = "max/Max.asm"

    parser = p.Parser(file)
    parser.file

    parser.readFile()
    parser.lines

    [parser.type(line) for line in parser.lines]
    [parser.symb(line) for line in parser.lines]
    dests = [parser.dest(line) for line in parser.lines]
    dests
    jumps = [parser.jump(line) for line in parser.lines]
    jumps
    comps = [parser.comp(line) for line in parser.lines]
    comps

    code = c.Code()

    [code.dest(dest) for dest in dests]
    [code.jump(jump) for jump in jumps]
    [code.comp(comp) for comp in comps]

    asm = Assembler(file)
    asm.pass1()
    asm.pass2()
    asm.out

if __name__ == '__main__':
    main(sys.argv[1])
