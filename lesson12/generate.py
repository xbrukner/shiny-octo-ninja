#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math, random, svgwrite

linesize = 20
startx = 30
starty = 30
walls = []
sizex = 8
sizey = 7
def printHex(startx, starty, wall):
	# 501
	# /-\
	# \_/
	# 432
	if wall[0]: svg.add( svg.line((startx, starty), (startx + linesize, starty), stroke="black") )
	if wall[1]: svg.add( svg.line((startx + linesize, starty), (startx + linesize + linesize / 2, starty + linesize * math.sqrt(3) / 2),  stroke="black") )
	if wall[2]: svg.add( svg.line((startx + linesize, starty + linesize * math.sqrt(3)), (startx + linesize + linesize / 2, starty + linesize * math.sqrt(3) / 2),  stroke="black") )
	if wall[3]: svg.add( svg.line((startx, starty + linesize * math.sqrt(3)), (startx + linesize, starty + linesize * math.sqrt(3)), stroke="black") )
	if wall[4]: svg.add( svg.line((startx, starty + linesize * math.sqrt(3)), (startx - linesize / 2, starty + linesize * math.sqrt(3) / 2),  stroke="black") )
	if wall[5]: svg.add( svg.line((startx, starty), (startx - linesize / 2, starty + linesize * math.sqrt(3) / 2),  stroke="black") )


def printArray():
	shifty = linesize * math.sqrt(3) / 2
	for i in range(sizey):
		mx = startx
		my = starty + linesize * math.sqrt(3) * i
		for j in range(sizex):
			printHex(mx, my, getWall(j, i))
			mx += linesize * 1.5
			my += -shifty if j % 2 else shifty

def createWalls():
	for i in range(sizex):
		for j in range(sizey):
			walls.append([True, True, True, True, True, True])

def getWallId(x, y):
	return y * sizex + x

def getWall(x, y):
	return walls[getWallId(x, y)]

def getNeighbour(x, y, wall):
	odd = x % 2
	even = int(not odd)
	if wall == 0: return (x, y - 1, 3)
	if wall == 1: return (x + 1, y - 1 * even, 4)
	if wall == 2: return (x + 1, y + 1 * odd, 5)
	if wall == 3: return (x, y + 1, 0)
	if wall == 4: return (x - 1, y + 1 * odd, 1)
	if wall == 5: return (x - 1, y - 1 * even, 2)

def inMaze(x, y):
	if x < 0 or x == sizex or y < 0 or y == sizey: return False
	return True

def removeWall(x, y, wall):
	walls[getWallId(x, y)][wall] = False
	n = getNeighbour(x, y, wall)
	if not inMaze(n[0], n[1]): return
	walls[getWallId(n[0], n[1])][n[2]] = False

visited = {}
def DFS(x, y):
	visited[(x, y)] = True
	order = range(6)
	random.shuffle(order)
	for n in order:
		neighbour = getNeighbour(x, y, n)
		if not inMaze(neighbour[0], neighbour[1]): continue
		if (neighbour[0], neighbour[1]) in visited: continue
		removeWall(x, y, n)
		DFS(neighbour[0], neighbour[1])

def putDots():
	r = linesize * math.sqrt(3) * 0.3
	svg.add( svg.circle( (startx + linesize / 2, starty + linesize * math.sqrt(3) / 2), r, stroke="blue"))
	shift = 0 if sizex % 2 else 0.5
	svg.add( svg.circle( (startx + (sizex - 1) * linesize * 1.5 + linesize / 2, starty + (sizey - 1 + shift) * linesize * math.sqrt(3) + linesize * math.sqrt(3) / 2), r, stroke="blue"))

createWalls()
DFS(0, 0)
svg = svgwrite.Drawing("tmp.svg")
printArray()
putDots()
svg.save()
