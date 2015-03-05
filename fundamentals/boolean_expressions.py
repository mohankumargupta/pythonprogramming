#Boolean expressions
#also referred to as logical operators in other programming languages
# https://docs.python.org/3/reference/expressions.html#boolean-operations

#and
'''
print('False and False is:', False and False)
print('False and True is:', False and True)
print('False and False is:' ,True and False)
print('False and False is:', True and True)
'''

#or
'''
print( False or False)
print( False or True)
print( True or False)
print( True or True)
'''

#not
'''
print(not True)
print(not False)
'''

a = 6
b = 7
c = 42
print(1, a == 6)
print(2, a == 7)
print(3, a == 6 and b == 7)
print(4, a == 7 and b == 7)
print(5, not a == 7 and b == 7)
print(6, a == 7 or b == 7)
print(7, a == 7 or b == 6)
print(8, not (a == 7 and b == 6))
print(9, not a == 7 and b == 6)



'''
print( 0 and 0)
print( 0 and 1)

print( 1 and 0)
print( 1 and 1)
'''



'''
print( 0 or 0)
print( 0 or 1)
print( 1 or 0)
print( 1 or 1)
'''


#evaluate to False
'''
print(bool( ""   ))
print(bool( None ))
print(bool( []   ))
print(bool( ()   ))
print(bool(  0   ))
print(bool(  0.0 ))
print(bool( -0.0 ))
'''

#evaluate to True
'''
print(bool( "abc"   ))
print(bool( [1,2,3]   ))
print(bool( (1,2,3)   ))
print(bool(  42   ))
print(bool(  4.2 ))
print(bool( -4.2 ))
'''

#type
'''
print(type( ""   ))
print(type( None ))
print(type( []   ))
print(type( ()   ))
print(type( 0    ))
print(type( 0.0  ))
print(type( {'one':1, 'two':2}  ))
'''

# combination of and, or and not
'''
print(False and True or True)
print(False and (True or True))
'''

# Hmmm....
'''
print("cat" and "dog")
print("cat" or "dog")
print("cat" or "dog" and "elephant")
print(("cat" or "dog") and "elephant")
print("cat" and "dog" and "elephant")
'''


'''
6.10. Boolean operations

or_test  ::=  and_test | or_test "or" and_test
and_test ::=  not_test | and_test "and" not_test
not_test ::=  comparison | "not" not_test

In the context of Boolean operations, and also when expressions are used by control flow statements, the following values are interpreted as false: False, None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true. User-defined objects can customize their truth value by providing a __bool__() method.

The operator not yields True if its argument is false, False otherwise.

The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.

The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

(Note that neither and nor or restrict the value and type they return to False and True, but rather return the last evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced by a default value if it is empty, the expression s or 'foo' yields the desired value. Because not has to create a new value, it returns a boolean value regardless of the type of its argument (for example, not 'foo' produces False rather than ''.)
'''

