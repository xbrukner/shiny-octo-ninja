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

def nilakantha(limit):
	result = 3.0
	dividend = 1
	for i in xrange(1, limit + 1):
		div = 2 * i
		result += (4.0 / (div * (div + 1) * (div + 2)) ) * dividend
		dividend *= -1
		
	return result
	
def archimedes(limit):
	a = 2.0 * math.sqrt(3)
	b = 3.0
	for i in xrange(0, limit):
		a = (2.0 * a * b) / (a + b)
		b = math.sqrt(a * b)
	return (a + b) / 2

def gauss_legendre(limit):
	a = 1.0
	b = 1.0 / math.sqrt(2)
	t = 0.25
	p = 1.0
	for i in xrange(0, limit):
		a_1 = (a + b) / 2
		b = math.sqrt(a*b)
		t = t - p * ((a - a_1) ** 2)
		p = 2*p
		a = a_1
	return ((a + b) ** 2) / (4 * t)

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
	limit = 1000
	print "Gregory Leibnitz:"
	print gregory_leibnitz(limit)
	print "Nilakantha:"
	print nilakantha(limit)
	print "Archimedes:"
	print archimedes(limit)
	print "Gauss_legedre:"
	print gauss_legendre(limit)
	print "Monte carlo:"
	print montecarlo(limit)
	print "math.pi"
	print math.pi
	
	return 0

if __name__ == '__main__':
	main()

