for line in open("test1.txt"):
    print(line, end='')
print('\n')

with open("test2.txt") as f:
    for line in f:
        print(line, end='')
print('\n')    


with open("test3.txt",'w') as f:
	f.write("Hello world\nHello World")