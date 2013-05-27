#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, numpy

def myCmp(x, y, c):
	return x if c(x, y) else y

def isFinite(x, y):
	#print x, y
	iteration = 50
	c = complex(x, y)
	z = 0
	mc = -5
	mr = -5
	cc = []
	cr = []
	for i in xrange(iteration):
		z = z**2 + c
		if abs(z) >= 2: return False
		mc = max(mc, z.imag)#myCmp(z, mc, lambda x, y: x.imag > y.imag)
		mr = max(mr, z.real)#myCmp(z, mr, lambda x, y: x.real > y.real)
		cc.append(z.imag)
		cr.append(z.real)
	return (True, numpy.mean(cr), numpy.mean(cc))

counter = 0
def view(startx, starty, stopx, stopy):
	size = (500, 500)
	stepx = (stopx - startx) / float(size[0])
	stepy = (stopy - starty) / float(size[1])
	values = {}
	im = Image.new( "RGB", size, (0,0,0) )
	minc = 10
	maxc = -10
	minr = 10
	maxr = -10
	for i in xrange(size[0]):
		for j in xrange(size[1]):
			c = isFinite(startx + i * stepx, starty + j * stepy)
			if c:
				values[(i, j)] = (c[1], c[2])
				minr = min(minr, c[1])
				maxr = max(maxr, c[1])
				minc = min(minc, c[2])
				maxc = max(maxc, c[2])
				#color = (128, int(c[1] * 255.0 / 2), int(c[2] * 255.0 / 2))
			else:
				color = (255, 255, 255)
				im.putpixel( (i, j), color)
	print maxc, minc, maxr, minr
	scalec = 255.0 / (maxc - minc)
	scaler = 255.0 / (maxr - minr)
	#print maxc, minc, maxr, minr
	for i in values:
		color = values[i]
		im.putpixel( i, (128, int(color[0] * scaler), int(color[1] * scalec)) )
	#im.show()
	global counter
	im.save("mandelbrot_%d.png" % counter)
	counter += 1

def main():
	view(-2, 2, 2, -2)
	view(-2, 1, 0, -1)
	view(-1, 0.5, 0, -.5)
	view(-1, 0, -0.5, -.5)
	view(-1 + 0.125, 0, -0.5 - 0.125, -.25)
	return 0

if __name__ == '__main__':
	main()

