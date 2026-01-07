d1 = {1:"a", 2:"b", 3:"c"}
d2 = {4:"x", 5:"y", 6:"z"}

d1.update(d2)
print(d1)

d3 ={}
for i in (d1,d2):
    d3.update(i)
print(d3)
