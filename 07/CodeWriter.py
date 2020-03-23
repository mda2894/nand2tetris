class CodeWriter:

    def __init__(self):
        self.out = list()
        self.jumpCount = 0
        self.arithmeticTable = {
            "add" : "M=D+M",
            "sub" : "M=M-D",
            "and" : "M=D&M",
            "or"  : "M=D|M",
            "neg" : "M=-M",
            "not" : "M=!M",
            "eq"  : "D;JEQ",
            "gt"  : "D;JGT",
            "lt"  : "D;JLT"
        }
        self.twoArgCalcList = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@SP",
            "M=M-1",
            "A=M",
            "cmd",
            "@SP",
            "M=M+1"
        ]
        self.oneArgCalcList = [
            "@SP",
            "M=M-1",
            "A=M",
            "cmd",
            "@SP",
            "M=M+1"
        ]
        self.comparisonList = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M-D",
            "@JUMP",
            "cmd",
            "@SP",
            "A=M",
            "M=0",
            "@EXIT",
            "0;JMP",
            "(JUMP)",
            "@SP",
            "A=M",
            "M=-1",
            "(EXIT)",
            "@SP",
            "M=M+1",
        ]
        self.pushConstantList = [
            "num",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]

    def writeArithmetic(self, arg):
        if arg in ["add", "sub", "and", "or"]:
            self.writeTwoArgCalc(arg)
        elif arg in ["neg", "not"]:
            self.writeOneArgCalc(arg)
        else:
            self.writeComparison(arg)

    def writePush(self, arg1, arg2):
        if arg1 == "constant":
            self.writePushConstant(arg2)

    def writeComment(self, comment):
        self.out.append("// " + comment)

    def writeTwoArgCalc(self, arg):
        cmd = self.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.twoArgCalcList]
        asm = "\n".join(asm)
        self.out.append(asm)

    def writeOneArgCalc(self, arg):
        cmd = self.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.oneArgCalcList]
        asm = "\n".join(asm)
        self.out.append(asm)

    def writeComparison(self, arg):
        cmd = self.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.comparisonList]
        asm = "\n".join(asm)
        asm = asm.replace("JUMP", "JUMP" + str(self.jumpCount))
        asm = asm.replace("EXIT", "EXIT" + str(self.jumpCount))
        self.out.append(asm)
        self.jumpCount += 1

    def writePushConstant(self, num):
        asm = ["@"+num if x == "num" else x for x in self.pushConstantList]
        asm = "\n".join(asm)
        self.out.append(asm)
