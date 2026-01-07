class A1:
    def myFunct1(self):
        print("Class A function called ")
class A2(A1):
    def myFunct2(self):
        print("Class B function called ")
class A3(A1):
    def myFunct3(self):
        print("Class C function called ")
c1 = A2()
c2 = A3()
c1.myFunct1()
c1.myFunct2()
c2.myFunct1()
c2.myFunct3()