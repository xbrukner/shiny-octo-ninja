#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, copy, svgwrite

def identity():
	return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def translation(x, y):
	r = identity()
	r[2][0] = x
	r[2][1] = y
	return r

def scale(x, y):
	r = identity()
	r[0][0] = x
	r[1][1] = y
	return r

def reflection(x, y):
	r = identity()
	if x: r[0][0] = -1
	if y: r[1][1] = -1
	return r

def rotation(a):
	r = identity()
	r[0][0] = math.cos(math.radians(-a))
	r[0][1] = math.sin(math.radians(-a))
	r[1][0] = -math.sin(math.radians(-a))
	r[1][1] = math.cos(math.radians(-a))
	return r

def sheer(k):
	r = identity()
	r[1][0] = k
	return r

#From http://stackoverflow.com/a/10508239
def matmult(a,b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]

def combine(l):
	r = identity()
	for t in l:
		tmp = copy.deepcopy(r)
		r = matmult(tmp, t)
	return r

def pointToMatrix(p):
	return [[p[0]], [p[1]], [1]]
def fromMatrix(m):
	return [ m[0][0], m[1][0] ]

def apply(num, action, lines, memory = False):
	current = copy.deepcopy(lines)
	result = copy.deepcopy(lines) if memory else []
	for i in xrange(num):
		new = []
		for i in current:
			r = [fromMatrix(matmult(action, pointToMatrix(i[0]))),
				fromMatrix(matmult(action, pointToMatrix(i[1])))]
			#print action, pointToMatrix(i[0]), matmult(action, pointToMatrix(i[0])), pointToMatrix(i[1]), matmult(action, pointToMatrix(i[1]))
			new.append(r)
			if memory: result.append(r)
		current = copy.deepcopy(new)
	return result if memory else current

def writelines(filename, lines):
	svg = svgwrite.Drawing(filename)
	for i in lines:
		svg.add( svg.line( (i[0][0] + 300, i[0][1] + 300), 
			(i[1][0] + 300, i[1][1] + 300), stroke="black") )
	svg.save()

action = combine([rotation(20), scale(1.1, 1.1), translation(30, 20)])
#action = translation(20, 30)
#action = combine([rotation(20), rotation(-20)])
#print action
start = [ ([0, 0], [100, 0]), ([0, 0], [0, 100]), ([100, 0], [100, 100]), ([0, 100], [100, 100]) ]
writelines("rotate.svg", apply(8, action, start, True))
#print combine([reflection(True, True), scale(4, 5), translation(2, -3)])
