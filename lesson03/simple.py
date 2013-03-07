#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import turtle
import math

def polygon(n, linesize = 100):
	inner_angle = (n - 2) * 180 / n
	
	t = turtle("polygon_"+str(n)+".svg", linesize, linesize, 0, True)
	for i in range(n):
		t.forward(linesize)
		t.right(180.0 - inner_angle) #Also 360.0 / n
	t.save()

def star(n, k, linesize = 100):
	t = turtle("star_"+str(n)+"_"+str(k)+".svg", linesize, linesize, 0, True)
	
	for i in range(n):
		t.forward(linesize)
		t.left(k * 360.0 / n)
		
	t.save()


def main():
	print("Enter number of vertices:")
	n = input()
	polygon(n)
	print("Enter parameter for star:")
	k = input()
	star(n, k)
	return 0

if __name__ == '__main__':
	main()

