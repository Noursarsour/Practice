#tuples
ram = ('Ram', 'green', 3)
fruits = ('ripe', 'red dellisious')
print(fruits[0])
for attribute in fruits:
    print(attribute)

#fruits[1]='bitter' not allowed, cannot change a tuple
fruits = (fruits[0], fruits[1], 'sweet') #make new tuple from old one
print(fruits)


#Sets
print(set(fruits))
fruits_set = {'bananna', 'apple', 'melon'} #unorderd
print(fruits_set)