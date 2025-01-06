words = ['hello', 'there', 'world']
print(id(words))
words_ = words
words.append('!')
print(words)
print(words_)
print(id(words_))

msg = 'hello'
msg = 'hi'  # ok! rebinds
#msg[0] = 'H' error immutable!
#id(words)

my_list = ['apple', 'berry','cherry']
your_list = my_list #shallow copy, same id
my_list.append('dutian')
print(my_list)
print(your_list)

from copy import deepcopy
your_list2 = deepcopy(my_list)
print(id(your_list))
print(id(your_list2))

your_list3 = my_list[:] #to make a copy with different id
print(id(your_list3))

def printLastElement(list): #it will modify the original list
    print(list.pop())
my_list2 = ['apple', 'berry','cherry']
printLastElement(my_list2)
print(my_list2)

from copy import copy
my_list2 = copy(my_list2) # or my_list[:]

a =[1,2]
b = [1,2]
print(a == b)
print(a is b)