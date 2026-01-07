import os 
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("file does not exit")