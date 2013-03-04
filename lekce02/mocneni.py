#!/usr/bin/env python
# -*- coding: utf-8 -*-

limit = 0.001
def exp_natural(a, b):
	#Calculate a^b, but stops when b >= 1 (and always subtract integers)
	if (a == 1):
		return 1
	exps = [1, a] #a ^ 0, a ^ 1...
	twos = [0, 1, 2] #2 ^ 0, 2 ^ 1...
	
	while twos[-1] < max(b, 1/limit): #Calculate a^2, a^3, a^4... a^ceil(log2 b) and the same series with base 2
		exps.append(exps[-1] * exps[-1])
		twos.append(twos[-1] * 2)
	
	start = len(exps) - 1
	res = 1
	while b >= 1:
		while twos[start] > b:
			start -= 1
		res *= exps[start]
		b -= twos[start]
	return (res, b)

def binary_guess(lower, upper, goal, func):
	#c = 0
	while True:
		guess = ((upper - lower) / 2.0) + lower
		result = func(guess)
		#c += 1
		#if c == 100: return result
		#print goal, result, guess
		if abs(goal - result) < limit:
			return guess
		if result > goal:
			upper = guess
		else:
			lower = guess

def exp1(a, b):	
	total, b = exp_natural(a, b)
	#Now b < 1, res = a ^ floor(b)
	exp2 = 10.0
	while b >= limit:
		root = int(round(b * exp2))
		b -= root / exp2
		inside, res = exp_natural(a, root)
		assert(res == 0)
		
		#exp2-th root of guess
		result = binary_guess(0, inside, inside, lambda x: exp_natural(x, exp2)[0])
		
		total *= result
		exp2 *= 10
		
	return total

def lna(a):
	#Calculates ln a
	#ln a = 2 * sum(n, 0, inf): ((x - 1)/(x + 1)) ^ (2*n + 1) * 1 / (2*n + 1)
	y = (a - 1) / (a + 1)
	powy = y
	result = 0
	for n in range(0, 100):
		result += powy / float(2*n + 1)
		powy *= y
		powy *= y
	return result * 2.0

def exp2(a, b):
	#a^x = sum(n, 0, inf): (x^n * ln^n a) / n!
	
	#Calculate ln a -> cannot guess, need e^a
	ln = lna(a)

	result = 1 #For n = 0
	divisor = 1 #n! = n(n - 1)!
	powb = 1 #b^n = b * (b ^ (n - 1))
	powln = 1 #ln^n
	for n in range(1, 100):
		powb *= b
		powln *= ln
		divisor *= n
		result += powb * powln / divisor
		
	return result
		
def main():
	a = input()
	b = input()
	print "Method 1 (guessing a^10):"
	print exp1(a, b)
	print "Method 2 (Taylor):"
	print exp2(a, b)
	print "Implicit pow:"
	print pow(a, b)
	return 0

if __name__ == '__main__':
	main()

