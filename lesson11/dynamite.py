#!/usr/bin/env python
# -*- coding: utf-8 -*-

import svgwrite

def load(filename):
	res = {}
	tr = {'.': (False, False), '#': (True, False), 'A': (False, True), 'B': (False, True) }
	c = 0
	for i in file(filename):
		for j in zip(range(len(i.strip())), i.strip()):
			t = tr[j[1]]
			res[(j[0], c)] = t[0]
			if t[1]: res[j[1]] = (j[0], c)
		c += 1
	return res

def neigh(i):
	return [ (i[0] - 1, i[1]), (i[0], i[1] - 1), (i[0] + 1, i[1]), (i[0], i[1] + 1) ]

def tupadd(i, j): return (i[0] + j[0], i[1] + j[1])
def tupmin(i, j): return i[1] < j[1] or i[0] < j[0]

def solve(maze):
	queue1 = [maze['A'] + (0,0)]
	queue2 = []
	solved = {}
	while maze['B'] not in solved:
		for i in queue1:
			for j in neigh(i):
				score = tupadd(i[2:], (1, 0))
				if j not in maze or (j in solved and tupmin(solved[j][2:], score)): continue
				solved[j[:2]] = i
				if maze[j]: queue2.append(j + score)
				else: queue1.append(j + score)
		queue1 = map(lambda x: x[:3] + (x[3] + 1,), queue2)
		queue2 = []
	return solved

m = load("blud")
s = solve(m)

def scale(p, m = (0, 0)): return (p[0] * 30 + m[0], p[1] * 30 + m[1])
svg = svgwrite.Drawing("maze.svg")
for i in m:
	if not isinstance(i, tuple): continue
	svg.add( svg.rect( scale(i), (30, 30), stroke="black", fill=("gray" if m[i] else "white") ) )

p = m['B']
while p != m['A']:
	svg.add( svg.line( scale(p, (15, 15)), scale(s[p], (15, 15)), stroke="blue") )
	p = s[p][:2]
	
svg.add( svg.text("A", insert=scale(m['A'], (4, 26)), font_size=30) )
svg.add( svg.text("B", insert=scale(m['B'], (6, 26)), font_size=30) )
svg.save()
