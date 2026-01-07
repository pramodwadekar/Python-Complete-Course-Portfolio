class A1:
    def myFunct1(self):
        print("Class A1 function called ")
class B1:
    def myFunct2(self):
        print("Class B1 function called ")
class C(A1,B1):
    def myFunct3(self):
        print("Class C1 function called ")
c1 = C()
c1.myFunct1()
c1.myFunct2()
c1.myFunct3()