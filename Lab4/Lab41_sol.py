# ---------
# PROBLEM 2
# ---------
#
# Write a Python function dir_info(dircetory) which returns two values:
#   (1) Number of files inside the directory (recursively!)
#   (2) Number of dirctories inside the directory (recursively)

#----------------------------------------------
# SOLUTION:
#----------------------------------------------

import os

# Based on recursion
def dir_info1(directory):
    nfiles, ndirs = 0, 0
    for file in os.listdir(directory):
        path = directory + "/" + file
        if os.path.isdir(path):
            ndirs += 1
            nf, nd = dir_info1(path)
            nfiles += nf
            ndirs += nd
        else:
            nfiles += 1

    return nfiles, ndirs

# Shorter solution based on os.walk
def dir_info2(directory):
    nfiles, ndirs = 0, 0
    for path, dirs, files in os.walk(directory):
        nfiles += len(files)
        ndirs += len(dirs)

    return nfiles, ndirs

if __name__ == "__main__":

    print dir_info1("c:/Anaconda")
    print dir_info2("c:/Anaconda")


