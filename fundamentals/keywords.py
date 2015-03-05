# List all keywords
'''
import keyword
print(keyword.kwlist)
'''

#True, False
'''
print(True == 1)
print(False == 0)
print(type(True))
print(type(False))
'''

#None
'''
print(type(None))
def boo():
	pass

someVariable = boo()
print(someVariable)
print(type(someVariable))
'''

#logical operators
'''
print( 1==1 and 2==1)
print( 1==1 and 2==2)
print( 1==1 or 2==1)
print( not 1==1)
'''

#as
'''
import keyword as mykeyword
print(mykeyword.kwlist)
'''

#assert (invariants)
'''
class Fund:
	def __init__(self, initial_amount):
		self.amount = initial_amount
	def transferMoney(self, fund, amount):
		self.amount = self.amount - amount
		fund.amount = fund.amount + amount
        

fund1 = Fund(100)
fund2 = Fund(200)
totalamountbeforetransfer = fund1.amount + fund2.amount
fund2.transferMoney(fund1, 50)
totalamountaftertransfer = fund1.amount + fund2.amount
assert(totalamountaftertransfer == totalamountbeforetransfer)
'''

#try, except, raise, finally
'''
try:
	assert(1==2)
except AssertionError:
	print('abort ship')
	#raise
else:
	pass
finally:
	pass
'''

#break
'''
for i in range(10):
	if (i < 5):
		print(i)
	else:
		break
'''

#continue
'''
for i in range(10):
	if (i < 5):
		continue
	else:
		print(i)
'''

#del
'''
a = 5
print(dir())
del a
print(dir())
'''

#is, is_not
'''
print(False == 0)
print(type(False))
print(type(0))
print(False is 0)
print(False is not 0)
'''

# in, not_in
'''
print(2 in [1,2,3])
print(5 in [1,2,3])
'''
