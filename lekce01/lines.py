#!/usr/bin/env python
# -*- coding: utf-8 -*-

import svgwrite

def lines(size, lines, filename = "lines.svg", int_bug = False):
	svg = svgwrite.Drawing(filename)
	divisor = 2 if int_bug else 2.0
	middle = size / divisor
	scale = middle / lines
	
	starts = ( #Starts of lines
		lambda x: ( x * scale, middle ),
		lambda x: ( middle, x * scale ),
		lambda x: ( size - x * scale, middle),
		lambda x: ( middle, size - x * scale)
	)
	ends = ( #Ends of lines
		lambda x: ( middle, middle - x * scale),
		lambda x: ( middle + x * scale, middle),
		lambda x: ( middle, middle + x * scale),
		lambda x: ( middle - x * scale, middle),
	)
	
	for it in range(0, 4):
		for i in range(0, lines):
			svg.add(svg.line( starts[it](i), ends[it](i), stroke = "black") )
	
	svg.save()
		
		

def main():
	lines (500, 10, "lines-normal.svg")
	lines (500, 30, "lines-dense.svg")
	lines (500, 30, "lines-dense-int.svg", True)
	return 0

if __name__ == '__main__':
	main()

