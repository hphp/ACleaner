#!/usr/bin/python
import random
import ac_detect
import time

move = [[0,1],[1,0],[0,-1],[-1,0]]

def run_random(startx,starty):
	c = 0
	while 1:
		ifo = [0,0,0,0]
		nextx = -1
		nexty = -1
		while 1:
			rand = random.randrange(4) 
			if ifo[rand] == 1 :
				continue
			nextx = startx + move[rand][0]
			nexty = starty + move[rand][1]
			if ac_detect.obstacle(nextx,nexty) == 1 :
				ifo[rand] = 1
			else:
				break
		print startx,starty
		startx = nextx
		starty = nexty
		c = c + 1
		if c > 100000:
			break

def run_straight(startx,starty):
	c = 0
	rand = 0
	while 1:
		ifo = [0,0,0,0]
		nextx = startx + move[rand][0]
		nexty = starty + move[rand][1]
		if ac_detect.obstacle(nextx,nexty) == 1 :
			ifo[rand] = 1
		while ifo[rand] == 1:
			rand = random.randrange(4) 
			nextx = startx + move[rand][0]
			nexty = starty + move[rand][1]
			if ac_detect.obstacle(nextx,nexty) == 1 :
				ifo[rand] = 1
		print startx,starty
		startx = nextx
		starty = nexty
		c = c + 1
		if c > 1000:
			break

#run_straight(50,50)
run_random(50,50)
