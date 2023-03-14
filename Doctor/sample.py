d = int(input("enter the number of rotation :"))
n = int (input("enter the number of elements :"))

arr = []

print("Enter the elements :")
for i in range(0, n):
    k = input()
    arr.append(k)

print(arr)

for i in range (0, d):
    temp = arr[0]
    for i in range (n):
        if i + 1 <n:
            arr[i]=arr[i+1]
        else:
            arr[i] = temp

print(arr)