#append operation 
lists =  ['apple','banana','cherry']
lists.append('orange')
print(lists)

#insert operation

#lists.insert('mango') ///this is error require 2 args, we put 1 args. 
# its requred (1,mango) 
lists.insert(1,'mango')
print(lists)
lists.insert(3,'graps')
print(lists)

#remove operation
lists.remove("mango")
print(lists)

#pop operation
lists.pop()
print(lists)

#delete operation
del lists[0]
print(lists)

lists.clear()
print(lists)