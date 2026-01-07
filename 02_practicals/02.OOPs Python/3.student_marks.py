class student():
    def __init__(self):
        self.name = input('Enter Student Name : ')
        self.marks= int(input('Enter Student Marks : '))
    def show(self):
        print('Student Name Is : ',self.name)
        print('Student Marks Is : ',self.marks)
    def result(self):
        if (self.marks >= 75):
            print('Great.. You Have distinction')
        elif (self.marks >= 60):
            print('Great.. You Have Fist Class')
        elif (self.marks >= 50):
            print('Great.. You Have Pass')
        else:
            print('Fail')
s1=student()
s1.show()
s1.result()  
