#!/bin/env/python
import time
import threading

x = 0
x_lock = threading.Lock()
def foo():
	x_lock.acquire()
	global x
	for i in xrange(100000000): x += 1
	x_lock.release()

def bar():
	x_lock.acquire()
	global x
	for i in xrange(100000000): x -= 1
	x_lock.release()

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
t1.start();
t2.start();
t1.join();
t2.join();
print x
