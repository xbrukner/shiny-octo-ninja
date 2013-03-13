#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import turtle
import math

def circles(n, down = False, linesize = 10):
	t = turtle("circle_"+str(n)+".svg", linesize, linesize, 0, True)
	
	angle = 360.0 / n
	absolute = 0
	
	for i in range(n * 5):
		diff = linesize * (math.sin(math.radians(absolute)) if down else math.cos(math.radians(absolute)))
		t.forward(linesize + diff)
		t.right(angle)
		absolute += angle
		if absolute >= 360.0:
			absolute = 0
	
	t.save()
	

def main():
	print("Enter number of vertices:")
	n = input()
	circles(n)
	return 0

if __name__ == '__main__':
	main()

