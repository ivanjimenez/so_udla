#!/usr/bin/env python

import subprocess
from sys import stdout, stderr
from os import linesep as nl

def gnuplot_ExecuteCommands (commands, data):
		args = ["gnuplot", "-e", (";".join([str(c) for c in commands]))]
		program = subprocess.Popen(\
						args, \
						stdin=subprocess.PIPE, \
						stdout=subprocess.PIPE, \
						stderr=subprocess.PIPE, \
						)
		for line in data:
				program.stdin.write(str(line)+nl)
		return program

def gnuplot_GifTest():
		commands = [\
						"set datafile separator ','",\
						"set terminal gif",\
						"set output",\
						"plot '-' using 1:2 with linespoints, '' using 1:2 with linespoints",\
						]
		data = [\
						"1,1",\
						"2,2",\
						"3,5",\
						"4,2",\
						"5,1"\
						]
		return (commands, data)

if __name__ == "__main__":
		(commands, data) = gnuplot_GifTest()
		plotProg = gnuplot_ExecuteCommands(commands,data)
		(out, err) = (plotProg.stdout, plotProg.stderr)
		stdout.write(out.read())
