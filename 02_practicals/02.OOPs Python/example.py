class student:
    def __init__(self):
        self.name = input('what is Your name = ')
        self.age = int(input('what is your age = '))
        self.marks = int(input('what is percentage = '))
    def show(self):
        print ("studen name is = ",self.name)
        print("student Age is = ",self.age)
        print("sudent marks is = ", self.marks)
    def per(self):
        if(self.marks>=35):
            print("you are Pass")

        else:
            print("you are Failed")
    def Age_cri(self):
        if(self.age<18):
            print("you are not eligible to drive")
        else:
            print('you are eligible to drive')
m1 = student()
m1.show()
m1.per()
m1.Age_cri()
    
