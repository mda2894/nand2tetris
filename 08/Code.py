class Code:

    def __init__(self):
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
        self.init = [
            "@256",
            "D=A",
            "@SP",
            "M=D"
        ]
        self.twoArgCalc = [
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
        self.oneArgCalc = [
            "@SP",
            "M=M-1",
            "A=M",
            "cmd",
            "@SP",
            "M=M+1"
        ]
        self.comparison = [
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
        self.pushConstant = [
            "num",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.pushLclArgThisThat = [
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
        self.popLclArgThisThat = [
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
        self.pushPointerTemp = [
            "@address",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.popPointerTemp = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@address",
            "M=D"
        ]
        self.pushStatic = [
            "@static",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.popStatic = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@static",
            "M=D"
        ]
        self.ifGoto = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@label",
            "D;JNE"
        ]
        self.callPush = [
            "@address",
            "D=M/A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.callEnd = [
            "@SP",
            "D=M",
            "@5",
            "D=D-A",
            "@nArgs",
            "D=D-A",
            "@ARG",
            "M=D",
            "@SP",
            "D=M",
            "@LCL",
            "M=D",
            "@func",
            "0;JMP",
            "(returnAddress)"
        ]
        self.Return = [
            "@LCL",
            "D=M",
            "@endFrame",
            "M=D",
            "@5",
            "D=D-A",
            "A=D",
            "D=M",
            "@retAddr",
            "M=D",
            "@SP",
            "A=M-1",
            "D=M",
            "@ARG",
            "A=M",
            "M=D",
            "@ARG",
            "D=M+1",
            "@SP",
            "M=D",
            "@endFrame",
            "AM=M-1",
            "D=M",
            "@THAT",
            "M=D",
            "@endFrame",
            "AM=M-1",
            "D=M",
            "@THIS",
            "M=D",
            "@endFrame",
            "AM=M-1",
            "D=M",
            "@ARG",
            "M=D",
            "@endFrame",
            "AM=M-1",
            "D=M",
            "@LCL",
            "M=D",
            "@retAddr",
            "A=M",
            "0;JMP"
        ]
