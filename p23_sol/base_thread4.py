#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

def imprime(cont, numhilo):
	while cont > 0:
		print "Hilo: %d Contando hacia atrás %d" % (numhilo, cont)
		cont -= 1
		time.sleep(5)
t1 = threading.Thread(target=imprime, args=(10,1))
t2 = threading.Thread(target=imprime, args=(4,2))
t3 = threading.Thread(target=imprime, args=(3,3))
t4 = threading.Thread(target=imprime, args=(7,4))

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

