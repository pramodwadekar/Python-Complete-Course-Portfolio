# l=Lock()

# The Lock object can be held by only one thread at a time. If any other thread wants 
# the same lock then it will have to wait until the other one releases it. It’s similar 
# to waiting in line to book a train ticket, public telephone booth etc.

# acquire() method: A Thread can acquire the lock by using acquire() method
# l.acquire()
# release() method: A Thread can release the lock by using release() method.
# l.release()


from threading import *
l=Lock()
l.acquire()
print("lock acquired")
l.release()
print("lock released")