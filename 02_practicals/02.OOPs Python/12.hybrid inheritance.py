class B1:
    def myFunct1(self):
        print("Class B1 function called ")
class B2(B1):
    def myFunct2(self):
        print("Class B2 function called ")
class B3(B1):
    def myFunct3(self):
        print("Class B3 function called ")
class B4(B2,B3):
    def myFunct4(self):
        print("Class B4 function called ")
c1 = B4()

c1.myFunct1()
c1.myFunct2()
c1.myFunct4()
c1.myFunct3()