import os
import sys
import time

child_pid = os.fork()
if child_pid == 0:
	os.system("ps -Af > ~/procesos.txt")
	time.sleep(5)
	sys.exit(0)

print "En el padre, el pid del hijo es %d" % child_pid
pid,status = os.waitpid(child_pid, 0)

print "Esperando volver, pid = %d, estado = %d" % (pid,status)
