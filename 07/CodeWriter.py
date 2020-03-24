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
        self.segmentTable = {
            "local"    : "LCL",
            "argument" : "ARG",
            "this"     : "THIS",
            "that"     : "THAT"
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
        self.pushLclArgThisThatList = [
            "@ind",
            "D=A",
            "@seg",
            "A=D+M",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.popLclArgThisThatList = [
            "@ind",
            "D=A",
            "@seg",
            "D=D+M",
            "@SP",
            "A=M-1",
            "D=D+M",
            "A=D-M",
            "M=D-A",
            "@SP",
            "M=M-1"
        ]
        self.pushPointerTempList = [
            "@address",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.popPointerTempList = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@address",
            "M=D"
        ]
        self.pushStaticList = [
            "@static",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.popStaticList = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@static",
            "M=D"
        ]

    def writeArithmetic(self, arg):
        if arg in ["add", "sub", "and", "or"]:
            self.writeTwoArgCalc(arg)
        elif arg in ["neg", "not"]:
            self.writeOneArgCalc(arg)
        else:
            self.writeComparison(arg)

    def writePush(self, arg1, arg2, file):
        if arg1 == "constant":
            self.writePushConstant(arg2)
        elif arg1 in ["local", "argument", "this", "that"]:
            self.writePushLclArgThisThat(arg1, arg2)
        elif arg1 in ["pointer", "temp"]:
            self.writePushPointerTemp(arg1, arg2)
        else:
            self.writePushStatic(arg2, file)

    def writePop(self, arg1, arg2, file):
        if arg1 in ["local", "argument", "this", "that"]:
            self.writePopLclArgThisThat(arg1, arg2)
        elif arg1 in ["pointer", "temp"]:
            self.writePopPointerTemp(arg1, arg2)
        else:
            self.writePopStatic(arg2, file)

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

    def writePushLclArgThisThat(self, seg, ind):
        asm = "\n".join(self.pushLclArgThisThatList)
        asm = asm.replace("ind", ind)
        asm = asm.replace("seg", self.segmentTable.get(seg))
        self.out.append(asm)

    def writePopLclArgThisThat(self, seg, ind):
        asm = "\n".join(self.popLclArgThisThatList)
        asm = asm.replace("ind", ind)
        asm = asm.replace("seg", self.segmentTable.get(seg))
        self.out.append(asm)

    def writePushPointerTemp(self, seg, ind):
        if seg == "pointer":
            address = str(3 + int(ind))
        else:
            address = str(5 + int(ind))
        asm = "\n".join(self.pushPointerTempList)
        asm = asm.replace("address", address)
        self.out.append(asm)

    def writePopPointerTemp(self, seg, ind):
        if seg == "pointer":
            address = str(3 + int(ind))
        else:
            address = str(5 + int(ind))
        asm = "\n".join(self.popPointerTempList)
        asm = asm.replace("address", address)
        self.out.append(asm)

    def writePushStatic(self, varnum, file):
        asm = "\n".join(self.pushStaticList)
        asm = asm.replace("static", file + "." + varnum)
        self.out.append(asm)

    def writePopStatic(self, varnum, file):
        asm = "\n".join(self.popStaticList)
        asm = asm.replace("static", file + "." + varnum)
        self.out.append(asm)
