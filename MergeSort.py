# MergeSort Ascending
def Mergesort(num):
    if len(num) > 1:
        mid = len(num)//2
        left = num[:mid]
        right = num[mid:]
        Mergesort(left)
        Mergesort(right)
        i = 0
        k = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                num[k] = left[i]
                i += 1
                k += 1
            else:
                num[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            num[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            num[k] = right[j]
            j += 1
            k += 1
num = [1,5,2]
Mergesort(num)
print(num)


# MergeSort Descending

def Mergesort(num):
    if len(num) > 1:
        mid = len(num)//2
        left = num[:mid]
        right = num[mid:]
        Mergesort(left)
        Mergesort(right)
        i = 0
        k = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                num[k] = left[i]
                i += 1
                k += 1
            else:
                num[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            num[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            num[k] = right[j]
            j += 1
            k += 1
num = [1,5,2]
Mergesort(num)
print(num)