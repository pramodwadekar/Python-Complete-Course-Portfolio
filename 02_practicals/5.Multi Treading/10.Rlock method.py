# To overcome the above problem of Simple Lock, we should go for RLock(Reentrant Lock). 
# Reentrant means the thread can acquire the same lock again and again. This will block 
# the thread only if the lock is held by any other thread. Reentrant facility is 
# available only for owner thread but not for other threads.

from threading import *
import time
l=RLock()
def factorial(n):
   l.acquire()
   if n==0:
       result=1
   else:
       result=n*factorial(n-1)
   l.release()
   return result

def results(n):
   print(" The Factorial of", n, "is:", factorial(n))

t1=Thread(target=results, args=(5,))
t2=Thread(target=results, args=(9,))

t1.start()
t1.join()
t2.start()