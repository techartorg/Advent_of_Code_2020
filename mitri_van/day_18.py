'''
--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71

Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51

Here are a few more examples:

	2 * 3 + (4 * 5) becomes 26.
	5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
	5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
	((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

Your puzzle answer was 11076907812171.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

	1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
	2 * 3 + (4 * 5) becomes 46.
	5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
	5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
	((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?

'''

test_data_1 = '2 * 3 + (4 * 5)'
test_data_2 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
test_data_3 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
test_data_4 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
test_data_5 = '(7 * 8 + 6 * 3) * 3 * 2 * ((5 + 7 * 8 * 8) * (9 + 6 * 9 * 7 + 6 * 7) + 8 + (7 + 2 + 3 + 7 * 5 * 5) * (5 + 8) + 5) * 6'


def evaluate_expression( raw_data, num = 0 ):
	prev_num = ''
	prev_op = ''

	result = 0
	sub_expression = 0
	mem_stack = [ ]

	data = list( raw_data.replace( ' ', '' ) )

	for char in data:
		if char == '(':
			sub_expression += 1

			if prev_num and result == 0:
				result = prev_num
			mem_stack.append( ( result, prev_op ) )
			prev_num = ''
			prev_op = ''
			result = 0

		elif char == ')':
			sub_expression -= 1
			prev_num = ''

			stored_val = mem_stack.pop( )

			if stored_val != ( 0, '' ):
				result = eval( '{0}'.format( stored_val[ 0 ] ) + stored_val[ 1 ] + '{0}'.format( result ) )

		elif char in [ '*', '/ ', '+', '-' ]:
			prev_op = char

		else:
			if prev_num and result != 0:
				result = eval( '{0}'.format( result ) + prev_op + char )

			elif not prev_num and result != 0 and prev_op:
				result = eval( '{0}'.format( result ) + prev_op + char )

			elif prev_num:
				result += eval( prev_num + prev_op + char )

			else:
				prev_num = char

	return result



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_18_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_18_input.txt'

	data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = input_file.read( ).strip( ).split( '\n' )

	result = 0
	results = [ ]
	for datum in raw_data:
		val = evaluate_expression( datum )
		results.append( val )

	result = sum( results )
	# result += evaluate_expression( test_data_5 )
	print( 'The result is: {0}'.format( result ) )



