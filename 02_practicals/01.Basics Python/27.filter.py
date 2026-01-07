def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))  
print(y)
print(list(y))

#short filter function
y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))


dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)