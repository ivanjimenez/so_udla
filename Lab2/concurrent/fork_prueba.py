import os

pid = os.getpid()
print "Comienza con PID: %d" % (pid)

forked_pid = os.fork()

if forked_pid == 0:
    print "Este process imprime la salida con PID: %d" % (forked_pid)
    print "Mi PID es: %d" % (os.getpid())

else:
    print "Este proceso tiene PID: %d" % (forked_pid)
