class animal:
    def move(self):
        pass
class Dog(animal):
    def move(self):
        print("i can bark")
class snake(animal):
    def move(self):
        print("i can hissss")
d=Dog()
s=snake()
d.move()
s.move()