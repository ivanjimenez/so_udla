#!/usr/bin/python

# ---------
# PROBLEM 1
# ---------
# Write a function dir_size(directory) which computes the total size in bytes of all files in a
# given directory (recursively!).
#
# def dir_size(directory):
#     # write your algorithm here
#     # compute the total size of files inside
#     # the directory
#     return size
#
# Hints:
# * Explore the os module: http://docs.python.org/2/library/os.html
# * Use the following funtions:
#       os.listdir, os.path, os.sep, os.path.isfile, os.path.normpath, os.path.getsize
# * Make sure to skip files which you have no permission to access!
#   In Windows, directories of type "JUNCTION" can cause problem to os.listdir()
#   Use try/except mechanism to overcome this problem
# * Use recursion !
# * Try to avoid os.walk() or else it will become trivial ...

#----------------------------------------------
# SOLUTION:
#----------------------------------------------

# We present two solutions:
# dir_size1   -   Based on recursin
# dir_size2   -   Based on os.walk
# 

import os

def dir_size1(dir):      # Using recursion
    size = 0
    try:
        files = os.listdir(dir)
    except:
        print "Skipping inaccessible directory:", dir
        return 0
    for file in files:
        path = dir + "/" + file
        path = os.path.normpath(path)
        if os.path.isfile(path):
            size += os.path.getsize(path)
        else:
            size += dir_size1(path)    # Recursive call !!
    return size

def dir_size2(dir):      # Using os.walk
    size = 0
    for path, dirs, files in os.walk(dir):
        for file in files:
            size += os.path.getsize(path + "/" + file)
    return size

if __name__ == "__main__":

    print dir_size1("c:/Anaconda")
    print dir_size2("c:/Anaconda")




