
class BankAccount(object):
	CURRENCY = 'AUD'

	def __init__(self, initialAmount):
		self.amount = initialAmount

	def withdrawAmount(self, amount):
		self.amount = self.amount - amount

	def depositAmount(self, amount):
		self.amount = self.amount + amount
	

class SwissBankAccount(BankAccount):
	pass

boo = SwissBankAccount(500)
print(boo.CURRENCY)
print(boo.amount)
boo.withdrawAmount(200)
assert boo.amount == 300, 'Something fishy going on'
#assert boo.amount == 400, 'Something fishy going on'

