import datetime
import random
def bubble_sort(ar):
    n = 0
    while n < len(ar):
        for i in range(len(ar)-1):
            if ar[i] > ar[i+1]:
                ar[i],ar[i+1] = ar[i+1],ar[i]
        n += 1
    return ar
N = 200
a = list(map(lambda n: random.randint(1,N+0*n),range(N)))
t1 = datetime.datetime.now()
b=bubble_sort(a)
t2 = datetime.datetime.now()
print(((t2-t1).microseconds))
print(b)
