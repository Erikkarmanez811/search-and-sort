from merge_sort import *
def search(ar,n):
    if len(ar) in [0,1]:
        if ar == []:
            print('error')
            return -1
        if ar[0] != n:
            print('error')
            return -1
    if n == ar[len(ar)//2]:
        return len(ar)//2

    if n > ar[len(ar)//2]:
        beer = search(ar[len(ar)//2+1:],n)
        if beer == -1:
            return -1
        return len(ar)//2+1+ beer
    if n < ar[len(ar)//2]:
        return search(ar[:len(ar)//2],n)
while True:
    raw_a =list( map(int,input().split()))
    a = merge_sort(raw_a)
    print(a)
    n = int(input())
    print(search(a,n))  
