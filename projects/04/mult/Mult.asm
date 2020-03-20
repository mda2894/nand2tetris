// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Pseudo-Code:
//
// out = 0
// if R1 == 0: return out
//  else:
// 	  while R0 > 0:
// 		out += R1
// 		R0 -= 1
//	  return out


// out = 0

	@R2
	M = 0 // RAM[R2] = 0
	
// if R1 == 0: return out

	@R1
	D=M // D = RAM[R1]
	
	@END
	D;JEQ // JMP to END if D = 0

// while R0 > 0

(LOOP)

	@R0
	D=M // D = RAM[R0]

	@END
	D;JEQ // JMP to END if D = 0

// out += R1

	@R1
	D=M // D = RAM[R1]

	@R2
	M=D+M // RAM[R2] += D

// R0 -= 1

	@R0
	M=M-1 // RAM[R0] -= 1

	@LOOP
	0;JMP // JMP to LOOP

(END)

	@END
	0;JMP