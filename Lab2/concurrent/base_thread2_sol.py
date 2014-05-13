import threading
import time


def imprime(cont, numhilo):
    while cont > 0:
        print "Hilo: %d Contando hacia atras %d " % (numhilo, cont)
        cont -= 1
        time.sleep(5)
 

t1 = threading.Thread(target=imprime, args=(5,1))

t2 = threading.Thread(target=imprime, args=(4,2))


t1.start(); t2.start()

t1.join(); t2.join()