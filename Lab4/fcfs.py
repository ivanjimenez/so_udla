#!/usr/bin/env python
''' Implementación del algoritmo de Planificación de Disco FCFS'''
import sys
import pdb

LEFT = "LEFT"
RIGHT = "RIGHT"

LOWER_CYLINDER = 0
UPPER_CYLINDER = 4999

def FCFS(requests, initialPosition):
	position = initialPosition
	movement = 0

	for x in range(len(requests)):
			movement += abs(position -requests[x])
			position = requests[x]
			print "Sirviendo a:" + str(position)
	
	return movement

#main
if __name__ == '__main__':
		requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
		initialPosition = int(sys.argv[1])
		print "\tFCFS = " + str(FCFS(requests, initialPosition))
