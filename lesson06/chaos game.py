#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, math, random

def getPolygon(n, x0, y0, linesize, size):
	k = linesize / (2.0 * math.sin (math.pi / n))
	pointx = lambda x: x0 + k * math.cos( x*2 * math.pi / n )
	pointy = lambda x: y0 + k * math.sin( x*2 * math.pi / n )
	point = lambda x: (size - int(round(pointy(x))), size - int(round(pointx(x))))
	
	points = []
	for i in range(n):
		points.append(point(i))
	print points
	return points

def cut(pointA, pointB, cut):
	return ( int(cut(pointA[0] + pointB[0])), int(cut(pointA[1] + pointB[1])) )

def cutColor(colorA, colorB):
	return ( (colorA[0] + colorB[0]) / 2, (colorA[1] + colorB[1]) / 2, (colorA[2] + colorB[2]) / 2 )

def chaos(size, n, linesize, offset, startPoint, iterations, cutRatio, colorfull = True):
	im = Image.new("RGB", (size, size), (255, 255, 255) )
	points = getPolygon(n, offset[0], offset[1], linesize, size)
	color = (0,0,0)
	point = startPoint
	#Generate random colors
	colors = {}
	if type(colorfull) == type([]):
		s = 0
		for i in points:
			colors[i] = colorfull[s]
			s += 1
	else:
		for i in points:
			colors[i] = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )
	
	print colors
	for i in xrange(iterations):
		whereTo = random.choice(points)
		new = cut(point, whereTo, cutRatio)
		if colorfull:
			color = cutColor(color, colors[whereTo])
		im.putpixel( new, color )
		point = new
	im.show()

def main():
	#scheme = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]
	#Sierpinski								
	#chaos(200, 3, 180, (91, 91), (75, 75), 100000, lambda x: x / 2, scheme )
	
	#Penta-flower
	#chaos(300, 5, 240, (10, 10), (150, 200), 100000, lambda x: x * 0.37, scheme)
	return 0

if __name__ == '__main__':
	main()
