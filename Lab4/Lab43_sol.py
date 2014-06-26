# ---------
# PROBLEM 3
# ---------
# Write a function find_string(s ,file) for finding all lines in file that contain the string s.
# You should report the line number and the line itself as in the following example:
#
#      file = "oliver_twist.txt"
#      find_string("Fagin", file)
#      =>
#         2616: 'Greenland. Is Fagin upstairs?'
#         2646: 'This is him, Fagin,' said Jack Dawkins;'my friend Oliver Twist.'
#         2723: Fagin! And why should they? It wouldn't have loosened the knot, or kept
#         2834: 'And what have you got, my dear?' said Fagin to Charley Bates.
#         2911: 'There, my dear,' said Fagin. 'That's a pleasant life, isn't it? They
#         3866: 'What'll Fagin say?' inquired the Dodger; taking advantage of the next
#         3929: Mr. Fagin looked so very much in earnest, that Charley Bates, who
#         . . .

#----------------------------------------------
# SOLUTION:
#----------------------------------------------

def find_string(s,file):
    f = open(file, 'r')
    n = 1
    for line in f:
        if s in line:
            print "%d: %s" % (n,line)
        n += 1
    f.close()


if __name__ == "__main__":

    find_string('FON', 'c:/Windows/system.ini')
