# Semaphore is advanced Synchronization Mechanism. Sometimes there might be requirements 
# where at a time a particular number of threads should be allowed to access the resources. 
# Like, at a time 10 members are allowed to access the database server or at a time 4 
# members are allowed to access Network connection. We can’t handle this requirement, 
# using Lock and RLock concepts. Hence, we should go for the Semaphore concept in such 
# cases.

from threading import *
import time
s=Semaphore(2)
def wish(name,age):
  for i in range(3):
      s.acquire()
      print("Hi",name)
      time.sleep(2)
      s.release()
t1=Thread(target=wish, args=("Sireesh",15))
t2=Thread(target=wish, args=("Nitya",20))
t3=Thread(target=wish, args=("Shiva",16))
t4=Thread(target=wish, args=("Ajay",25))
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()
t4.start()