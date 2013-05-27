#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, svgwrite

def load(filename):
	res = []
	for i in file(filename):
		res.append(map(lambda x: float(x) * 50, i.split(' ')))
	return res

points = load("linreg.txt")
n = len(points)

sumx = sum(map(lambda n: n[0], points))
sumy = sum(map(lambda n: n[1], points))
sumxs = sum(map(lambda n: n[0] ** 2, points))
sumxy = sum(map(lambda n: n[0] * n[1], points))

a = (n * sumxy - sumx*sumy) / (n * sumxs - sumx ** 2)
b = (sumxs * sumy - sumx * sumxy) / (n * sumxs - sumx ** 2)
line = lambda x: a*x + b
print a, b

svg = svgwrite.Drawing("linreg.svg")
for i in points:
	svg.add( svg.circle(( i[0] + 200, i[1] + 200), r=1, stroke="blue") )
svg.add( svg.line( (0, line(-200) + 200), ( 400, line(200) + 200), stroke="black") )
svg.save()
