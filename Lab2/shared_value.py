import threading
import time
import logging

x = 0           # x Compartido
def foo():
    global x
    for i in xrange(100000000): x += 1

def bar():
    global x
    for i in xrange(100000000): x -= 1

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
t1.start(); t2.start()
t1.join(); t2.join()   # Espera a que se completen
print x                # El resultado esperado es 0