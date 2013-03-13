#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import turtle
import math

def bush(n, linesize = 100, t = False, recurse = 0):
	if recurse == n:
		return
	
	if not t:
		t = turtle("bush_"+str(n)+".svg", linesize, linesize * 2, 90, True)
	
	angle = 360.0 / n
	
	t.forward(linesize)
	t.left(angle)
	bush(n, linesize / 2.0, t, recurse + 1)
	t.right(angle + 180 + angle)
	bush(n, linesize / 2.0, t, recurse + 1)
	t.left(angle)
	t.forward(linesize)
	
	if not recurse:
		t.save()


def main():
	bush(4)
	bush(5)
	bush(6)
	bush(8)
	bush(9)
	return 0

if __name__ == '__main__':
	main()

