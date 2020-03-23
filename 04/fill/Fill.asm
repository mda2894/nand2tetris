// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Pseudo-Code:
//
// repeat:
//   if kbd == last:
//     continue
//   else:
//     last = kbd
//     if kbd = 0:
//	     white()
//     else:
//       black()
//
// def white():
//   for (i in 0:8192) {screen[i] = 0}
// def black():
//   for (i in 0:8192) {screen[i] = -1}
//

	@last
	M=0 // RAM[last] = 0
	
	@24576
	D=A // D = 24576
	
	@end
	M=D // RAM[end] = 24576

(START)
	
	@last
	D=M // D = RAM[last]
	
	@KBD
	D=D-M // D = RAM[last]-RAM[KBD]
	
	@START
	D;JEQ // JMP to START if RAM[KBD] == RAM[last]
	
	@KBD
	D=M // D = RAM[KBD]
	
	@last
	M=D // RAM[last] = RAM[KBD]
	
	@WHITE
	D;JEQ // JMP to WHITE if RAM[KDB] == 0
	
	@BLACK
	D;JNE // JMP to BLACK is RAM[KBD] != 0
	
(WHITE)

	@SCREEN
	D=A // D = SCREEN (16384)
	
(LOOPW)
	
	@end
	D=D-M // D = D - end
	
	@START
	D;JEQ // JMP to START if D == end
	
	@end
	D=D+M 
	A=D
	M=0 // if D != end, RAM[D] = 0
	
	D=D+1 // D=D+1
	
	@LOOPW
	0;JMP // JMP to LOOPW

(BLACK)

	@SCREEN
	D=A // D = SCREEN (16384)
	
(LOOPB)
	
	@end
	D=D-M // D = D - end
	
	@START
	D;JEQ // JMP to START if D == end
	
	@end
	D=D+M 
	A=D
	M=-1 // if D != end, RAM[D] = -1
	
	D=D+1 // D=D+1
	
	@LOOPB
	0;JMP // JMP to LOOPB