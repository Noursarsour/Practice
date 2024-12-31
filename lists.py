#Iteration
#lists: ordered, mutable collection of items
name = "Nour"
print(list(name))

for char in name:
    print(char)

tup = (1,3,49)
for item in tup:
    print(item)

dict= {'a': 30, 'b':15}
print(list(dict))
for item in dict:
    print(item)


ingredients=["apple", "strawberry", "orange"]
ingredients[0]= "kiwi"
ingredients.append('peach')
print(ingredients)
print(len(ingredients))

print("apple" in ingredients)
print("kiwi" in ingredients)
print(ingredients[2])
print(ingredients[len(ingredients)-1]) #last item in the list
print(ingredients[-1]) #last item in the list

ingredients.extend(["melon", "cantalope"])
print(ingredients)

#removed = ingredients.pop()
#print(ingredients)
#print(removed)

#while ingredients:
    #current = ingredients.pop() #pop(0)
    #print(current.upper())

#print(ingredients)

#del ingredients[0]

ingredients.sort() #modifies the list in place, it does not create a new list
#do not set sort() to a variable, it is going to be none.
print(ingredients)
