d = {1: 'apple', 2: 'banana', 3: 'strawberry'}
print(d)

# create dictionary using { }
d1 = {1: 'apple', 2: 'banana', 3: 'strawberry'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "apple", b = "banana", c = "strawberry")
print(d2)

# Access using key
print(d[1])

# Access using get()
print(d.get(3))

# Adding a new key-value pair
d[2] = [3,2,"apple"]

# Updating an existing value
d[1] = "Python"

print(d)

# Using del to remove an item
del d[1]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(3)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)