# multiplication all atoms in a dictionary

d3 = {"a":4, "b":5, "c":9}
print(sum (d3.values()))

id = [1,2,3,4,5]
name = ["pramod", "kunal", "mayur", "saurav", "yash"]
d1 =dict()
for i in id:
    for j in name:
        d1.update({i:j})
print("dictionary",d1)    