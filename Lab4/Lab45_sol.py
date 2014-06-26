#!/usr/bin/python

import os, sys, fnmatch

def find_files(startdir, pattern):
    for path, dirs, files in os.walk(startdir):
        for file in files+dirs:
            if fnmatch.fnmatch(file, pattern):
                print os.path.join(path, file)

##### Execution:

argc = len(sys.argv)   # Arguments count (number of arguments) including the command itself!

if not argc == 3:
    print "Usage: find_files.py directory pattern"
    sys.exit(1)

directory = sys.argv[1]
pattern = sys.argv[2]
find_files(directory, pattern)




