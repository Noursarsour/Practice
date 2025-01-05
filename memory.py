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