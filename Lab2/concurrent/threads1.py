import threading
import time
count = 1
class KissThread(threading.Thread):
    def run(self):
        global count
        print "Thread # %s: Intentando hacer hilos" % count
	count += 1
	time.sleep(2)
	print "hecho"
for t in range(5):
	KissThread().start()

