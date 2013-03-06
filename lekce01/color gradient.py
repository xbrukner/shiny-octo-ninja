#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image

def colorGradient(size, filename = ""):
	color = lambda x,y: (int(x), 0, int(y))
	img = Image.new("RGB", (size, size))
	scale = 255.0 / size
	
	for i in range(0, size):
		for j in range(0, size):
			img.putpixel( (i, j), color(i * scale, j * scale) )
	if not filename:
		img.show()
	else:
		img.save(filename)

def main():
	print "Enter size in pixels:"
	size = input()
	colorGradient(size)
	print "Save to file? (enter filename, or leave blank):"
	save = raw_input()
	if save:
		colorGradient(size, save)
	return 0

if __name__ == '__main__':
	main()
