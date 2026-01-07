lists = ["apple","banana","cherry"]
print (lists)
for i in lists:
    print("length is with for loop : ",len(i))
print ("length of without for loop : ",len(lists))

print(lists[1])

lists[2] ="blackbery"
print(lists)

if "apple" in lists:
    print("yes apple in this list")

lists1 = ['graps','orange',]
lists.extend(lists1)
print(lists)

lists3 = lists.copy()
print(lists3)

lists4 = list(lists1)
print(lists4) 

a = [12,4,18,78,99,23,30,2]
max = 0
for i in a:
    if i>=max:
        max=i
print(max)