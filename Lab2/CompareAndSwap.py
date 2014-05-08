import random
import time
from threading import *
import pdb

class RefVar():
  def __init__(self):
    self.val=0
    
bolt = RefVar()

def CandS(word,test,new):
  old=word.val
  if (old==test): word.val = new
  return old

class Proc(Thread):
  def __init__(self,label):
    Thread.__init__(self)
    self.label=label
  def start(self):
    Thread.start(self)
  def run(self):
    #global bolt
    while (True):
      while (CandS(bolt,0,1)==1): print "%s waits on bolt=%d" % (self.label,bolt.val)
      # critical section
      print "%s enters critical region" % self.label
      i=10000
      while i<0: i-=1
      print "%s leaves critical region" % self.label
      bolt.val=0
      # other stuff
      print "%s enters non-critical region" % self.label
      sleep=random.randint(0,10)
      time.sleep(sleep)
      print "%s leaves non-critical region" % self.label


P1 = Proc('P1')
P2 = Proc('  P2')
P3 = Proc('    P3')

pdb.set_trace()

P1.start()
P2.start()
P3.start()

P1.join()
P2.join()
P3.join()
