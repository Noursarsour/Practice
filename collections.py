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
fruits_set.add('peach')
print(fruits_set)
fruits_set.remove('melon')
print(fruits_set)
print(fruits_set.pop(), 'pop')
print(fruits_set)

letters= list('happy')
print(letters)
letters_set = set('happy')
print(letters_set)

#
#int()
#float()
#type()
#str()

#list of tuples
animals = [('Instance', 'gray', 2), ('Ram', 'green', 2), ('Unicode', 'blue', 2)]
print(animals[1])
print(animals[0][1])
print(animals)

#Comprehensions
words = ['awesome', 'alex', 'orange', 'ant', 'deadly']
upper_words =[]
for word in words:
    upper_words.append(word.upper())
print(upper_words)
upper_words_comprehension = [word.upper() for word in words]

a_words = []
for word in words:
    if word.startswith('a'):
        a_words.append(word)
a_word_comprehension = [word for word in words if word.startswith('a')]

#[word.upper() for word in words if word.startswith('a')]
#[expression for item in list if condition]
#[expression for item in list if condition]
US_STATES_POPULATIONS =[]
big_states = set()
for population in US_STATES_POPULATIONS:
    if population > 1000000:
        big_states.add(population)

big_states = {population
              for population in US_STATES_POPULATIONS
              if population > 1000000}