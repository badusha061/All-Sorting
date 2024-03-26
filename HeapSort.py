# Ascending Order

def heapify(arr , n , i):
    largest = i
    left = (i * 2) + 1
    right = (i * 2) + 2
    if  left < n and  arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if i != largest:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 -1 , -1 , -1):
        heapify(arr , n , i)
    for i in range(n -1 , 0 , -1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr , i , 0)

num = [1,5,2]
heapsort(num)
print(num)


#Desending Order
def heapify(arr , n , i):
    largest = i
    left = (i * 2) + 1
    right = (i * 2) + 2
    if  left < n and  arr[left] < arr[largest]:
        largest = left
    if right < n and arr[right] < arr[largest]:
        largest = right
    if i != largest:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 -1 , -1 , -1):
        heapify(arr , n , i)
    for i in range(n -1 , 0 , -1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr , i , 0)

num = [1,5,2]
heapsort(num)
print(num)
