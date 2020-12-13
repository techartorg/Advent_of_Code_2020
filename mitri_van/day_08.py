'''
--- Day 8: Handheld Halting ---

Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

	acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
	jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
	nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

For example, consider the following program:

	nop +0
	acc +1
	jmp +4
	acc +3
	jmp -3
	acc -99
	acc +1
	jmp -4
	acc +6

These instructions are visited in this order:

	nop +0  | 1
	acc +1  | 2, 8(!)
	jmp +4  | 3
	acc +3  | 6
	jmp -3  | 7
	acc -99 |
	acc +1  | 4
	jmp -4  | 5
	acc +6  |

First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

Your puzzle answer was 1810.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

Your puzzle answer was 969.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

ACCUMULATOR = 0
INST_COUNT_ACC = 0
INST_COUNT_JMP = 0
INST_COUNT_NOP = 0

test_data = [ ( 'nop', '+0' ),
				  ( 'acc', '+1' ),
				  ( 'jmp', '+4' ),
				  ( 'acc', '+3' ),
				  ( 'jmp', '-3' ),
				  ( 'acc', '-99' ),
				  ( 'acc', '+1' ),
				  ( 'jmp', '-4' ),
				  ( 'acc', '+6' ) ]


def acc( val ):
	global ACCUMULATOR
	global INST_COUNT_ACC

	INST_COUNT_ACC += 1
	ACCUMULATOR += val


def jmp( line_num, val ):
	global INST_COUNT_JMP

	INST_COUNT_JMP += 1
	line_num += val

	return line_num


def nop( ):
	global INST_COUNT_NOP
	INST_COUNT_NOP += 1


def patch_code( instruction ):
	if 'jmp' in instruction:
		instruction = ( 'nop', instruction[ 1 ] )
	elif 'nop' in instruction:
		instruction = ( 'jmp', instruction[ 1 ] )

	return instruction


def code_patcher( data ):
	fix_lines = [ line for line in enumerate( data ) if line[ 1 ][ 0 ] in [ 'jmp', 'nop' ] ]

	for fix in fix_lines:
		line_num = 0
		patch_data = data.copy( )

		fix_line = fix[ 0 ]
		instruction = patch_code( fix[ 1 ] )
		# instruction = patch_data[ instruction_num - 1 ]
		patch_data[ fix_line ] = instruction

		line_num = run( patch_data )
		if line_num >= len( data ):
			return fix_line


def run( data ):
	global ACCUMULATOR
	ACCUMULATOR = 0
	count_acc = 0
	count_jmp = 0
	count_nop = 0

	data_size = len( data )
	instructions = [ ]
	line_num = 0

	while line_num < data_size:
		curr_instruction = line_num + 1
		if line_num not in instructions:
			instructions.append( line_num )
		else:
			print( '\t\t>>>> EOL' )
			return line_num

		cmd = data[ line_num ][ 0 ]
		val = int( data[ line_num ][ 1 ] )

		if cmd == 'acc':
			count_acc += 1
			line_num += 1
			acc( val )

		elif cmd == 'jmp':
			count_jmp += 1
			line_num = jmp( line_num, val )

		elif cmd == 'nop':
			count_nop += 1
			line_num += 1
			nop( )
		# print( '[ {0} ]\tACC: {1}\tJMP: {2}\tNOP: {3}'.format( curr_instruction, INST_COUNT_ACC, INST_COUNT_JMP, INST_COUNT_NOP ) )

	return line_num



if __name__ == "__main__":
	# input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_08_input.txt'
	input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_08_input.txt'

	data = [ ]
	line_num = 0

	with open( input, 'r' ) as input_file:
		instruction = [ tuple( line.strip( ).split(  ) ) for line in input_file.readlines( ) ]
		data += instruction

	line_num = run( data )
	line_num_patch = code_patcher( data )

	print( '\nAccumulator: {0}'.format( ACCUMULATOR ) )
	print( 'Exit on line: {0}'.format( line_num ) )

	print( 'Patch on line: {0}'.format( line_num_patch ) )

