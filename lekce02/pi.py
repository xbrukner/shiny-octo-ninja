#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, random

def gregory_leibnitz(limit):
	#4* sum(n, 0, inf): (-1)^n / (2n + 1)
	dividend = 1
	divisor = 1
	result = 0.0
	for i in xrange(0, limit):
		result += (4.0 / divisor) * dividend
		dividend *= -1
		divisor += 2
	return result

def archimedes(limit):
	a = 2.0 * math.sqrt(3)
	b = 3.0
	for i in xrange(0, limit):
		a = (2.0 * a * b) / (a + b)
		b = math.sqrt(a * b)
	return (a + b) / 2

def montecarlo(limit):
	good = 0
	bad = 0
	for i in xrange(0, limit):
		x = random.random()
		y = random.random()
		if x**2 + y ** 2 < 1:
			good += 1
			
	return (4 * good) / float(limit)

def main():
	limit = 1000000
	print "Gregory Leibnitz:"
	print gregory_leibnitz(limit)
	print "Archimedes:"
	print archimedes(limit)
	print "Monte carlo:"
	print montecarlo(limit)
	print "math.pi"
	print math.pi
	
	return 0

if __name__ == '__main__':
	main()

