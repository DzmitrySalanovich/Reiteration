b = []
a = 9
for i in range(a):
    b.append(i)
    i=i+1

list_a = [i**2 for i in b]
print(list_a)


num = range(20)
dd = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, num))      
print(list(dd))

