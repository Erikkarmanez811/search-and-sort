def merge(ar,ra):
    i = 0
    j = 0
    re= []
    while i != len(ar) and j != len(ra):
        if ar[i] < ra[j]:
            re.append(ar[i])
            i += 1
        else:
            re.append(ra[j])
            j += 1
    re += ar[i:] + ra[j:]
    return re



def merge_sort(ar):
    if len(ar) == 1:
        return ar
    return merge(merge_sort(ar[:len(ar)//2]),merge_sort(ar[len(ar)//2:]))
    

