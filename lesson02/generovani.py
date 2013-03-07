#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gen(inp, used, combination, reuse, length, s = "\t"):
	if len(used) == length: #All used -> end recursion
		print s
		return
	searched = [] #Used only for combinations
	for i in inp:
		if combination and searched != used: #Only print elements after the first one (for combinations)
			if i in used:
				searched.append(i)
			if searched != used: continue

		if not reuse and i in used: #Do not print already used numbers (for not reuse)
			continue
			
		gen(inp, used + [i], combination, reuse, length, s + str(i) + " ")

def main():
	a = input()
	b = input()
	assert (b <= a)
	
	arr = range(0, a)
	print "Permutations:"
	gen(arr, [], False, False, a)
	print "Combinations (len = ", b, "):"
	gen(arr, [], True, False, b)
	print "Combinations with repetition (len = ", b, "):"
	gen(arr, [], True, True, b)
	print "Variations (len = ", b, "):"
	gen(arr, [], False, False, b)
	print "Variations with repetition (len = ", b, "):"
	gen(arr, [], False, True, b)
	return 0

if __name__ == '__main__':
	main()
