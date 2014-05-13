import os
import sys
import time

pid_hijo = os.fork()

if pid_hijo == 0:

	os.system('ps -Af > ~/procesos.txt')
	time.sleep(5)
	sys.exit(0)

print "En el padre, el pid del hijo es %d" % pid_hijo
pid, status = os.waitpid(pid_hijo,0)
os.system('mv ~/procesos.txt ~/proc.txt')
print "Tarea finalizada, pid = %d, estado = %d" % (pid,status)
