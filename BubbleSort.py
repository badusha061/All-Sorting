
# ascending order
def Bubblesort(num):
    for i in range(len(num)-1,0,-1):
        print(i)
        for j in range(i):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
num = [1,5,2]   
Bubblesort(num)
print(num)


#Decending Order
def Bubblesort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] < num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
num = [1,5,2]
Bubblesort(num)
print(num)