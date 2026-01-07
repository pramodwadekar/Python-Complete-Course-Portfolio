class criteria():
    def __init__(self):
        self.name = int(input("what is your age = "))
    def show(self):
        if(self.name >= 18):
            print("you are eligible")
        else:
            print("you are not eligible")
s1=criteria()
s1.show()