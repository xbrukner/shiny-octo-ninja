#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, svgwrite, random
colors = [ "red", "black", "blue", "green", "orange" ]

def load(filename, fun = lambda: False):
	res = {}
	for i in file(filename):
		res[tuple(map(lambda x: float(x) * 10, i.split(' ')))] = fun()
	return res

def distance(a, b):
	return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def assign(centers, points):
	res = {}
	change = False
	for i in points:
		cs = map(lambda x: distance(x, i), centers)
		c = min(xrange(len(centers)), key = cs.__getitem__) #http://stackoverflow.com/a/11825864
		res[i] = c
		if c is not points[i]: change = True
	return (res, change)

def move(centers, points):
	data = [(0, 0, 0) for i in range(centers)]
	sumdata = lambda p, d: (p[0] + d[0], p[1] + d[1], d[2] + 1)
	for i in points.items():
		data[i[1]] = sumdata(i[0], data[i[1]])
	return map(lambda d: (d[0] / d[2], d[1] / d[2]) if d[2] else (0, 0), data)

cs = 5
points = load("cluster_data.txt", lambda: random.choice(range(cs)))
for i in xrange(100):
	centers = move(cs, points)
	(points, change) = assign(centers, points)
	if not change: break
print i

svg = svgwrite.Drawing("cluster.svg")
for i in points:
	svg.add( svg.circle(( i[0] + 200, i[1] + 200), r=5, stroke=colors[points[i]], fill=colors[points[i]]) )
for i in zip(xrange(len(centers)), centers):
	svg.add( svg.rect( ((i[1][0] - 5) + 200, i[1][1] - 5 + 200), (10, 10), stroke="black", fill=colors[i[0]]) )
svg.save()
