import Parser as p, Code as c

file = "StackArithmetic\StackTest\StackTest.vm"

parser = p.Parser(file)

parser.readFile()

parser.lines

[parser.type(line) for line in parser.lines]
[parser.arg1(line) for line in parser.lines]
[parser.arg2(line) for line in parser.lines]
