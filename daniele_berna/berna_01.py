import itertools
import functools

def brute_force(my_in):
	"""
	Don't joke! :-)
	"""
	for i in range(len(my_in)):
		for j in range(i+1,len(my_in)):
			if my_in[i]+my_in[j]==2020:
				return(my_in[i]*my_in[j])

def find_index(my_in):
	"""
	This just for part 1
	"""
	for i in range(len(my_in)):
		try:
			res = my_in.index(2020-my_in[i],i+1)
			if res:
				return my_in[i]*my_in[res]
		except:
			pass

def check_combinations(my_in, size):
	"""
	This is fine! :-)
	"""
	return [functools.reduce(lambda a,b : a*b,comb) for comb in set(itertools.combinations(my_in, size)) if sum(comb)==2020]

my_input = [int(d) for d in open('./input_01.txt', 'r').read().split()]

#print(brute_force(my_in))
#print(find_index(my_in))

print(f"Part 1: {check_combinations(my_input, 2)}")
print(f"Part 2: {check_combinations(my_input, 3)}")

