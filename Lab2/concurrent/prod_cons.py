from threading import Lock, Condition
from collections import deque

items      = deque()
items_cv   = Condition()

def producer():
    while True:
         # produce some item
         items_cv.acquire()
         items.append(item)
         items_cv.notify()
         items_cv.release()

def consumer():
    while True:
         items_cv.acquire()
         while not items:
               items_cv.wait()
         item = items.popleft()
         items_cv.release()
         # Do something with item
