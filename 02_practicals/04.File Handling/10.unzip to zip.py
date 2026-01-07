from zipfile import *
f=ZipFile("file.zip","w")
f.write("file.txt")
print("done")
f.close()