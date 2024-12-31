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
print(sorted(ingredients)) #it does not modify the original list


#list slicing
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[:])
print(nums[:0]) #empty
print(nums[:-1])
print(nums[2:6])
print(nums[6:])
print(nums[:7])
print(nums[::2]) #step
print(nums[::-1])
print(nums[-2:])
print(nums[:-2])

#range
for number in range(5):
    print(number)

print(list(range(10)))
print(range(10, 4))
print(list(range(10, 2, -1)))

for index, item in enumerate(ingredients):
    print(index, item)
for index in range(len(ingredients)):
    print(index, ingredients[index])
