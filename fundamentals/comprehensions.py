#list comprehension

'''
double = [i*2 for i in range(10)]
print(double)
'''

'''
double = [[i, i*2] for i in range(10)]
print(double)
'''

#print(dir(__builtins__))
#random_list = [ random.random() for i in range(3) ]


'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from math import sqrt;

def pythagTriplet1():
	for a in range(500):
		for b in range(a+1, 500):
			if ((pow(a, 2) + pow(b, 2)) == pow(1000-a-b, 2)):
				print("a:" + str(a) + " b:" + str(b) + " c:" + str(1000-a-b))
				return a*b*(1000-a-b)

#print(pythagTriplet1())

def pythagTriplet2():
   	return [(a, b, 1000-a-b) for a in range(1, 500) for b in range(1, a) if sum([a,b,1000-a-b]) == 1000 and (a*a + b*b == (1000-a-b)*(1000-a-b)) ]

#print(pythagTriplet2())

#comprehending comprehensions
someDictionary = {'a':1, 'b':3, 'c':6}
sortedSomeDictionary = sorted(someDictionary.items(),key=lambda x: x[0])
print(someDictionary)
print(sortedSomeDictionary)
print(''.join([b*a for (a,b) in sortedSomeDictionary]))

