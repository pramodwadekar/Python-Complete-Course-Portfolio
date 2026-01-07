import threading
def print_hello(n):
    print("hello, how old are you ?",n)
t1 = threading.Thread(target=print_hello,args=(20,))
t2 = threading.Thread(target=print_hello,args=(28,))
t1.start()
t1.join()
t2.start()