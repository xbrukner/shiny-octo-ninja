#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image, math

def circle_filled(r):
	size = r * 2
	im = Image.new("RGB", (size, size) )
	for x in range(size):
		for y in range(size):
			if (x - size / 2) ** 2 + (y - size / 2) ** 2 <= r**2:
				im.putpixel( (x,y), (0,0,0) )
			else:
				im.putpixel( (x,y), (255, 255, 255) )
	im.save('circle_filled.png')

def circle_slow(r):
	size = r * 2
	width = 100
	im = Image.new("RGB", (size, size) )
	for x in range(size):
		for y in range(size):
			if abs((x - size / 2) ** 2 + (y - size / 2) ** 2 - r**2) < width:
				im.putpixel( (x,y), (0,0,0) )
			else:
				im.putpixel( (x,y), (255, 255, 255) )
	im.save('circle_slow.png')

def circle_fast(r):
	size = r * 2 + 10
	im = Image.new("RGB", (size, size), (255,255,255) )
	sampling = 30
	for i in range(360 * sampling):
		x = int(math.sin(math.radians(i / sampling))*r + size / 2)
		y = int(math.cos(math.radians(i / sampling))*r + size / 2)
		im.putpixel( (x, y), (0,0,0) )
	im.save('circle_fast.png')

def spiral(r):
	size = r * 2 + 10
	halfsize = size/2
	im = Image.new("RGB", (size, size), (255,255,255) )
	sampling = 6
	for i in range(360 * sampling):
		x = int(math.sin(math.radians(i))*r* (i/(sampling*360.0)) + size / 2)
		y = int(math.cos(math.radians(i))*r* (i/(sampling*360.0)) + size / 2)
		c_r = abs(y - halfsize) * 255 / halfsize
		c_g = (halfsize - x if x < halfsize else 0) * 255 / halfsize
		c_b = (-halfsize + x if x > halfsize else 0) * 255 / halfsize
		#print c_r,c_g,c_b
		#r = g = b = 255
		im.putpixel( (x, y), (c_r,c_g,c_b) )
	im.save('spiral.png')

def main():
	circle_slow(100)
	circle_fast(100)
	circle_filled(100)
	spiral(100)
	return 0

if __name__ == '__main__':
	main()

