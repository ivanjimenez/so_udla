import os

parent_pid = os.getpid()
print "[parent] comienza con PID: %d" % (parent_pid)

forked_pid = os.fork()

if forked_pid == 0:
	print "[child] el proceso hijo no puede utilizar os.fork() PID, desde su %d" % (forked_pid)
	print "[child] pero si puede realizar os.getpid() para conocer su propio PID: %d" % (os.getpid())
else:
	print "[parent] El proceso padre ha creado un hijo con PID: %d" % (forked_pid)
