#!/usr/bin/env python
# -*- coding: utf-8 -*-

import svgwrite, math

class turtle:
	
	def __init__(self, filename = "drawing.svg", x = 0, y = 0, angle = 0, pen = False):
		self.svg = svgwrite.Drawing(filename)
		self.x = float(x)
		self.y = float(y)
		self.angle = float(angle)
		self.pen = float(pen)
	
	def forward(self, step):
		return self.move(step, True)
	
	def backward(self, step):
		return self.move(step, False)
	
	def penup(self):
		self.pen = False
	
	def pendown(self):
		self.pen = True
	
	def right(self, angle):
		return self.shift(-angle)
	
	def left(self, angle):
		return self.shift(angle)
	
	def shift(self, angle):
		self.angle += angle
		while (self.angle < 0): self.angle += 360.0
		while (self.angle > 360): self.angle -= 360.0
	
	def move(self, step, forward):
		stepx = math.cos(math.pi / 180.0* self.angle) * step
		stepy = - math.sin(math.pi / 180.0 * self.angle) * step
		
		if forward:
			newx = self.x + stepx
			newy = self.y + stepy
		else:
			newx = self.x - stepx
			newy = self.y - stepy
		
		if self.pen:
			self.svg.add( self.svg.line( (self.x, self.y), (newx, newy), stroke="black") )
		
		#print self.angle, self.x, self.y, newx, newy, stepx, stepy
		self.x = newx
		self.y = newy
	
	def save(self):
		self.svg.save()

def main():
	
	return 0

if __name__ == '__main__':
	main()

