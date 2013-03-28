#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import turtle

class Lsystem:
	def __init__(self, start, rules, semantics):
		self.state = start
		self.rules = rules
		self.semantics = semantics
	
	def expand(self, steps):
		for i in xrange(steps):
			res = ''
			for i in self.state:
				if i in self.rules:
					res += self.rules[i]
				else:
					res += i
			self.state = res
	
	def draw(self, filename, start):
		t = turtle(filename, start[0], start[1])
		t.pendown()
		for i in self.state:
			self.semantics[i](t)
		t.save()

def main():
	l_sierp = Lsystem( "A", {'A': 'B-A-B', 'B': 'A+B+A'},
	 { 'A': lambda t: t.forward(5), 
	 'B': lambda t: t.forward(5),
	 '+': lambda t: t.right(60),
	 '-': lambda t: t.left(60) })
	l_sierp.expand(20)
	l_sierp.draw('/tmp/l_sierp.svg', (300, 300) )
	
	return 0

if __name__ == '__main__':
	main()

