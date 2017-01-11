def insertion_sort(ar):
    for i in range(1,len(ar)):
        while i>0 and ar[i] < ar[i-1]:
            ar[i],ar[i-1] = ar[i-1],ar[i]
            i-=1
    return ar
a = [3,6,45,7,8,12,1,1,1,1,1,1,2,-1000]
print(insertion_sort(a))

    
    

        
    
