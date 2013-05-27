#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def simulate(change):
	choices = [True, False, False]
	mine = random.choice(choices)
	return not mine if change else mine

def sequence(num, fun):
	good = 0
	for i in xrange(num):
		if simulate(fun()):
			good += 1
	return (good, num)

print "Staying:"
print "%d successful" % sequence(100, lambda: False)[0]
print "Changing:"
print "%d successful" % sequence(100, lambda: True)[0]
print "Random:"
print "%d successful" % sequence(100, lambda: random.choice([False, True]))[0]
