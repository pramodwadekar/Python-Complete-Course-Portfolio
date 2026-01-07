from zipfile import *
f= ZipFile ("file.zip","r")
f.extractall()
f.close()