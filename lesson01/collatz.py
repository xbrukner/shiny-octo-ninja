#!/usr/bin/env python
# -*- coding: utf-8 -*-

def SVGHeader():
	print '<?xml version="1.0" standalone="no"?>\
 <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\
 <svg width="100%" height="100%" version="1.0"\
 xmlns="http://www.w3.org/2000/svg">'
 
def SVGFooter():
	print '</svg>'
	
def addPoint(sizeX, sizeY, valX, valY, maxX, maxY):
	#print valY
	cx = (sizeX / float(maxX))
	cy = (sizeY / float(maxY))
	r = 2
	#assert(valX * cx <= sizeX)
	assert(valY * cy <= sizeY)
	x = 10 + valX * cx
	y = sizeY - valY * cy 
	print '<circle cx="{x}" cy="{y}" r="{r}" style="fill:black" />'.format(x=x, y=y, r=r)
	#print '<text x="{x}" y="{y}">{valY}</text>'.format(x=x, y=y, r=r, valY=valY)

def collatz(num):
	counter = 0
	max = num
	while num > 1:
		if num % 2:
			num = 3 * num + 1
		else:
			num /= 2
		counter += 1
		max = num if num > max else max
	return (counter, max)

SVGHeader()
mode = "height"
if mode == "height":
	maxX = 10000
	maxY = 0
	for i in range(2, maxX):
		num = collatz(i)[0]
		maxY = num if num > maxY else maxY
	for i in range(2, maxX):
		addPoint(1900, 800, i, collatz(i)[0], maxX, maxY)
elif mode == "maximum":
	maxX = 1000
	maxY = 0
	for i in range(2, maxX):
		num = collatz(i)[1]
		maxY = num if num > maxY else maxY
	for i in range(2, maxX):
		addPoint(1000, 800, i, collatz(i)[1], maxX, maxY)
SVGFooter()
