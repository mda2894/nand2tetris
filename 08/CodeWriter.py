import Code as c

class CodeWriter:

    def __init__(self):
        self.out = list()
        self.jumpCount = 0
        self.code = c.Code()
        self.functionName = ""

    def writeComment(self, comment):
        self.out.append("// " + comment)

    def writeInit(self):
        self.writeComment("Init")
        asm = "\n".join(self.code.init)
        self.out.append(asm)

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

    def writeLabel(self, arg1):
        asm = "(" + self.functionName + "$" + arg1 + ")"
        self.out.append(asm)

    def writeGoto(self, arg1):
        asm = "@" + self.functionName + "$" + arg1 + "\n" + "0;JMP"
        self.out.append(asm)

    def writeIfGoto(self, arg1):
        asm = "\n".join(self.code.ifGoto)
        asm = asm.replace("label", self.functionName + "$" + arg1)
        self.out.append(asm)

    def writeTwoArgCalc(self, arg):
        cmd = self.code.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.code.twoArgCalc]
        asm = "\n".join(asm)
        self.out.append(asm)

    def writeOneArgCalc(self, arg):
        cmd = self.code.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.code.oneArgCalc]
        asm = "\n".join(asm)
        self.out.append(asm)

    def writeComparison(self, arg):
        cmd = self.code.arithmeticTable.get(arg)
        asm = [cmd if x == "cmd" else x for x in self.code.comparison]
        asm = "\n".join(asm)
        asm = asm.replace("JUMP", "JUMP" + str(self.jumpCount))
        asm = asm.replace("EXIT", "EXIT" + str(self.jumpCount))
        self.out.append(asm)
        self.jumpCount += 1

    def writePushConstant(self, num):
        asm = ["@"+num if x == "num" else x for x in self.code.pushConstant]
        asm = "\n".join(asm)
        self.out.append(asm)

    def writePushLclArgThisThat(self, seg, ind):
        asm = "\n".join(self.code.pushLclArgThisThat)
        asm = asm.replace("ind", ind)
        asm = asm.replace("seg", self.code.segmentTable.get(seg))
        self.out.append(asm)

    def writePopLclArgThisThat(self, seg, ind):
        asm = "\n".join(self.code.popLclArgThisThat)
        asm = asm.replace("ind", ind)
        asm = asm.replace("seg", self.code.segmentTable.get(seg))
        self.out.append(asm)

    def writePushPointerTemp(self, seg, ind):
        if seg == "pointer":
            address = str(3 + int(ind))
        else:
            address = str(5 + int(ind))
        asm = "\n".join(self.code.pushPointerTemp)
        asm = asm.replace("address", address)
        self.out.append(asm)

    def writePopPointerTemp(self, seg, ind):
        if seg == "pointer":
            address = str(3 + int(ind))
        else:
            address = str(5 + int(ind))
        asm = "\n".join(self.code.popPointerTemp)
        asm = asm.replace("address", address)
        self.out.append(asm)

    def writePushStatic(self, varnum, file):
        asm = "\n".join(self.code.pushStatic)
        asm = asm.replace("static", file + "." + varnum)
        self.out.append(asm)

    def writePopStatic(self, varnum, file):
        asm = "\n".join(self.code.popStatic)
        asm = asm.replace("static", file + "." + varnum)
        self.out.append(asm)
