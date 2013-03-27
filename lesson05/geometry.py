#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math, random, svgwrite

size = 400
length = 200
lines = []
intersections = []
e = 0.00001
points = []

def clear():
	lines[:] = []
	intersections[:] = []
	points[:] = []

def generate_lines(number):
	#Generate number of random lines with the same length
	for i in range(number):
		while True:
			x1 = random.random() * size
			y1 = random.random() * size
			angle = random.random() * 360
			x2 = x1 + length * math.cos(math.radians(angle))
			y2 = y1 + length * math.sin(math.radians(angle))
			if  (0 <= x2 < size) and (0 <= y2 < size):
				lines.append( ((x1, y1), (x2, y2)) )
				break

def generate_points(number):
	#Generate number of points
	for i in range(number):
		x = random.random() * size
		y = random.random() * size
		points.append( (x, y) )

def pointOnLine(line, point):
	#Is point in rectangle, which diagonal is given as line?
	((x1, y1), (x2, y2)) = line
	(x, y) = point
	if (x1 <= x2):
		if not (x1 <= x <= x2): return False
	else:
		if not (x2 <= x <= x1): return False
	
	if (y1 <= y2):
		if not (y1 <= y <= y2): return False
	else:
		if not (y2 <= y <= y1): return False
	
	return True

def lineSharedEnd(line1, line2):
	#Shared endings of two line segments?
	return (line1[0] == line2[0] or line1[0] == line2[1] or
		line1[1] == line2[0] or line1[1] == line2[1])
	

def intersects(i, j):
	#Return point of intersection, if there is intersection between two line segments
	((x1, y1), (x2, y2)) = i
	((x3, y3), (x4, y4)) = j
	divisor = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
	if abs(divisor) < e: return False
	dividend_x = (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)
	dividend_y = (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)
	x = dividend_x / divisor
	y = dividend_y / divisor
	point = (x, y)
	#No intersection on the line segments -> not between the line endings
	if not pointOnLine(i, point) or not pointOnLine(j, point): return False
	return point

def find_intersections():
	#Find all intersections between lines
	done = []
	for i in lines:
		for j in lines:
			if j in done: continue
			point = intersects(i, j)
			if point:
				intersections.append(point)
		done.append(i)

def save(filename):
	#Save SVG to file
	svg = svgwrite.Drawing(filename)
	for i in points:
		svg.add( svg.circle(i, r=1, stroke="blue") )
	for i in lines:
		svg.add( svg.line(i[0], i[1], stroke="black") )
	for i in intersections:
		svg.add( svg.circle(i, r=3, stroke="blue") )
	svg.save()

def triangulate():
	#Triangulation - take lines from one starting point to every other and then move to another starting point
	done = []
	for i in points:
		for j in points:
			if j in done: continue
			good = True
			for l in lines:
				if not lineSharedEnd(l, (i, j)) and intersects(l, (i, j)):
					good = False
					break
			if good:
				lines.append( (i, j) )
		done.append(i)

def linelength(start, end):
	#Return the length of line (given by starting point and ending point) -> Pythagoras theorem
	return math.sqrt( (start[0] - end[0])**2 + (start[1] - end[1])**2 )

def triangulate_sorted():
	#Triangulation - lines sorted by length
	done = []
	alllines = []
	
	for i in points:
		for j in points:
			if j in done: continue
			alllines.append( (i, j) )
		done.append(i)
	
	alllines.sort( lambda x, y: int(linelength(x[0], x[1]) - linelength(y[0], y[1])) )
	
	for p in alllines:
		good = True
		for l in lines:
			if not lineSharedEnd(l, p) and intersects(l, p):
				good = False
				break
		if good:
			lines.append(p)
		

def anglePoints(a, b):
	#Returns a tangent of an absolute angle of vector from a to b
	return math.atan2( (b[1] - a[1]),  (b[0] - a[0]) ) 
	#WORKS ONLY if a is right of b

def rightOf(a, b):
	return a[0] > b[0]

def leftOf(a, b):
	return a[0] < b[0]

def convex_hull():
	leftmost = (size, size)
	rightmost = (0, 0)
	for i in points:
		if i[0] < leftmost[0]:
			leftmost = i
		if i[0] > rightmost[0]:
			rightmost = i
	while not len(lines) or rightmost != lines[-1][1]:
		start = lines[-1][1] if len(lines) else leftmost
		end = False
		for i in points:
			if i == start: continue
			if not rightOf(i, start): continue
			if not end:
				end = i
				continue
			if anglePoints(start, end) < anglePoints(start, i):
				end = i
		lines.append( (start, end) )

	while leftmost != lines[-1][1]:
		start = lines[-1][1]
		end = False
		for i in points:
			if i == start: continue
			if not leftOf(i, start): continue
			if not end:
				end = i;
				continue
			if anglePoints(end, start) < anglePoints(i, start):
				end = i
		lines.append( (start, end) )
	return
			
			

def main():
	#Intersections
	generate_lines(20)
	find_intersections()
	save("intersection.svg")
	clear()
	
	#Triangulation
	generate_points(20)
	triangulate()
	save("triangulation.svg")
	clear()
	
	#Triangulation - sorted by length
	generate_points(20)
	triangulate_sorted()
	save("triangulation_sorted.svg")
	clear()
	
	#Convex hull
	generate_points(20)
	convex_hull()
	save("convex_hull.svg")
	return 0

if __name__ == '__main__':
	main()
