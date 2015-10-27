#chars and ints
print(ord('a'))
print(ord('a') + 2)
print(chr(ord('a') + 2))

# string to list
print(list("123"))
print(list("abc"))
print(list("oh goody!"))

#list to tuple
print(tuple(['a','b','c']))

#dictionary to list of tuples
print(list({'a':1,'b':2,'c':3}.items()))

#key and value lists to dictionary
keys = ['a','b','c']
values = [1, 2, 3]
print(dict(zip(keys,values)))

