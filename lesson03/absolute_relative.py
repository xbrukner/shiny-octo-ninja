#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import turtle
import math
import svgwrite

def star_pentagon_relative(linesize = 100):
	
	t = turtle("pentagon_relative.svg", linesize, linesize, 0, True)
	for i in range(5):
		t.forward(linesize)
		t.right(360.0 / 5)
	
	# A   B  C
	# ----===
	#     \ |
	#      \|D
	# I need to rotate to go from A to D
	# The triangle ABD is over two vertices ->
	#  B is inner angle and the remaining angles are the same
	t.right( 36 ) # 180 - 108 (inner angle) / 2
	#I also need to expand linesize - it has to be distance from A to D:
	# linesize = AB = BD
	# BC = BD * cos(72)
	# CD = BD * sin(72)
	# AD = sqrt((ab + bc)^2 + CD^2)
	bc = linesize * math.cos(math.pi / 180.0 * 72)
	cd = linesize * math.sin(math.pi / 180.0 * 72)
	ad = math.sqrt((linesize + bc) ** 2 + cd ** 2)
	
	for i in range(5):
		t.forward(ad)
		t.left(3 * 360.0 / 5)
	t.save()

def star_pentagon_absolute(linesize = 100):
	svg = svgwrite.Drawing("pentagon_absolute.svg")
	
	x0 = linesize + 100
	y0 = linesize + 100
	k = linesize / (2.0 * math.sin (math.pi / 5.0))
	
	pointx = lambda x: x0 + k * math.cos( x*2 * math.pi / 5 )
	pointy = lambda x: y0 + k * math.sin( x*2 * math.pi / 5 )
	point = lambda x: (pointx(x), pointy(x))
	
	#Make line between every two vertices
	for i in range(5):
		for j in range(5):
			if i == j: continue
			svg.add(svg.line( point(i), point(j), stroke = "black" ))
	
	svg.save()

def spiral_relative(linesize = 100, angle = 20, outer = 10):
	t = turtle("spiral_relative.svg")
	t.pendown()
	
	for i in range(outer):
		for j in range(4):
			t.forward(linesize)
			t.right(90)
			
		d = math.radians(angle)
		# degree = angle ACD
		# BC = AD
		#A---D 
		# | /
		#C|/
		# |
		#B----
		# AC + AD = linesize
		# AD / AC = tan (degree)
		# CD = AD / sin (degree)
		
		ad = linesize * math.tan(d) / (1 + math.tan(d))
		ac = linesize - ad
		cd = ad / math.sin(d) #math.sqrt(ac ** 2  + ad ** 2)
				
		t.forward(ad)
		t.right(angle)
		linesize = cd
	t.save()
	
def circle_absolute(diameter = 200, lines = 20):
	svg = svgwrite.Drawing("circle_absolute.svg")
	
	start = 20
	radius = diameter / 2.0
	center = radius + start
	step = diameter / float(lines)
	
	
	for i in range(1, lines + 1):
		from_center = radius - i * step
		half_length = math.sin( math.acos(abs(from_center) / radius)) * radius
		
		#Horizontal line
		svg.add(svg.line( (center - half_length, center + from_center), (center + half_length, center + from_center), stroke = "black" ))
		#Vertical line
		svg.add(svg.line( (center + from_center, center - half_length), (center + from_center, center + half_length), stroke = "black" ))
	
	svg.save()

def triangle_relative(length = 200, triangles = 15):
	t = turtle("triangle_relative.svg", 20, 20 + length * math.sqrt(3) / 2, 0, True)
	move = length / triangles
	
	while (length > 0):
		for i in range(3):
			t.forward(length)
			t.left(120)
		t.penup()
		t.left(30)
		t.forward(move)
		t.right(30)
		t.pendown()
		
		length -= math.cos( math.radians(30) ) * move * 2
	t.save()

def flower(n = 12, diameter = 200):
	t = turtle("flower_relative.svg", diameter / 4.0 + 20, diameter / 4.0 + 20, 0, True)
	degree = 360.0 / n
	length = diameter / float(n)
	
	for i in range(n):
		for j in range(n):
			t.forward(length)
			t.right(degree)
		t.right(degree)
	t.save()

def main():
	star_pentagon_relative()
	star_pentagon_absolute()
	spiral_relative(100, 16, 15)
	circle_absolute()
	triangle_relative()
	flower()
	return 0

if __name__ == '__main__':
	main()

