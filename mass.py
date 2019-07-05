b = []
a = 9
for i in range(a):
    b.append(i)
    i=i+1
print(b)

w = 3
h = 4
c = 0
a = [[0 for x in range(w)] for y in range(h)] 
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = c
        c = c + 1
print(a)