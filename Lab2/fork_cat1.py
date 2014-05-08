import os

pid = os.getpid()
print "[PADRE] Comienza con PID: %d" % (pid)

forked_pid = os.fork()

if forked_pid == 0:
	print "[HIJO] Este proceso imprime la salida con PID: %d" % (forked_pid)
	print "[HIJO] Mi PID es: %d" % (os.getpid())
else:
	print "[PADRE] Este proceso tiene PID: %d" % (forked_pid)
