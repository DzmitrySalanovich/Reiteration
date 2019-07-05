class Iterator:
    def __iter__(self):
        return self
    
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

n = int(input())
print(" ")

s = Iterator(n)
for i in s:
    print(i)