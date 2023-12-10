# Ascending Order
def SelectionSort(num):
    for i in range(len(num)):
        min_pos = i
        for j in range(i+1):
            if num[j] > num[min_pos]:
                min_pos = j
        num[i],num[min_pos] = num[min_pos],num[i]

num = [1,5,2]
SelectionSort(num)
print(num)


# Descending Order
def SelectionSort(num):
    for i in range(len(num)):
        min_pos = i
        for j in range(i+1):
            if num[j] < num[min_pos]:
                min_pos = j
        num[i],num[min_pos] = num[min_pos],num[i]

num = [1,5,2]
SelectionSort(num)
print(num)