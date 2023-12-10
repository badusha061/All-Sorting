# Quick Sort Acending
def partition(num,low,high):
    p = num[low]
    i = low + 1
    j = high
    while True:
        while i <= j and num[i] <= p:
            i += 1
        while i <= j and num[j] >= p:
            j -= 1  
        if i < j:
            num[i],num[j] = num[j],num[i]
        else:
            break
    num[low],num[j] = num[j],num[low]
    return j  
        
def Quicksort(num,low,high):
    if low < high:
        pivot = partition(num,low,high)
        Quicksort(num,low,pivot-1)
        Quicksort(num,pivot+1,high)

num = [1,5,2]
low = 0
high = len(num)-1
Quicksort(num,low,high)
print(num)

# Quck Sort Decending
def partition(num,low,high):
    p = num[low]
    i = low + 1
    j = high
    while True:
        while i <= j and num[i] >= p:
            i += 1
        while i <= j and num[j] <= p:
            j -= 1  
        if i < j:
            num[i],num[j] = num[j],num[i]
        else:
            break
    num[low],num[j] = num[j],num[low]
    return j  
        
def Quicksort(num,low,high):
    if low < high:
        pivot = partition(num,low,high)
        Quicksort(num,low,pivot-1)
        Quicksort(num,pivot+1,high)

num = [1,5,2]
low = 0
high = len(num)-1
Quicksort(num,low,high)
print(num)