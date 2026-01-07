class A:
    def myFunct(self):
        print("Class A function called ")
class B(A):
    def myFunct2(self):
        print("Class B function called ")
class C(B):
    def myFunct3(self):
        print("Class C function called ")
c1 = C()
c1.myFunct2()
c1.myFunct()
c1.myFunct3()