f=open("file.txt","w")
try:
    f.write("hello world")
finally:
    f.close()