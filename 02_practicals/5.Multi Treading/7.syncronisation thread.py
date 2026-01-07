# Synchronization between threads

# Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously 
# execute some particular program segment known as critical section

#syncronisation is done by two ways :
# 1. using locks method
# 2. using semophore method

# lock :- The library provides a simple-to-implement locking mechanism that allows 
# us to synchronize threads. A new lock is created by calling the Lock() method, 
# which returns the new lock.