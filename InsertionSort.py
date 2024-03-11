num = [1,5,2]

#ascending order
for i in range(1,len(num)):
    key = num[i]
    j = i -1 
    while j >= 0 and key < num[j]:
        num[j+1] = num[j]
        j = j - 1
    num[j+1] = key


#descending order
for i in range(1,len(num)):
    key = num[i]
    j = i -1 
    while j >= 0 and key < num[j]:
        num[j+1] = num[j]
        j = j - 1
    num[j+1] = key
