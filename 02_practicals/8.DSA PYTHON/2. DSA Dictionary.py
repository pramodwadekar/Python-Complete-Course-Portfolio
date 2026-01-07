# Tip := Dictionary is also called HASHMAP or associative array in other progamming 
# languages

student = {"name":"mark","age":"20","DOB":"4-8-2000"}
print(student)
print (student['name'])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("email","Not Found"))
student["age"] = "23" # age change...
print(student)

#print(student.pop()) # pop expected at least 1 argument, got 0

print(student.pop('name'))
print(student) #name is remove

print(len(student))

print(student.pop('age'))
print(student) #age is remove