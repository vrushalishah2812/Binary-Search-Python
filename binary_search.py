def binary_search(arr,num) :
    temp = 0
    first = 0
    last = len(arr) - 1
    mid = int((first + last)/2)
    while first <= last :
        if arr[mid] < num :
            first = mid + 1
        elif arr[mid] == num :
            print("Your number {} is on {} position.".format(num,mid+1))
            temp = 1
            break
        elif arr[mid] > num :
            last = mid-1
        mid = int((first + last)/2)
    if temp == 0 :
        print("Choosed Number {} is not in the Array.".format(num))

binary_array =[]
no = int(input("Enter total number : "))
for i in range(1,no+1) :
    temp = int(input("Enter {} number : ".format(i)))
    binary_array.append(temp)
binary_array.sort()
print("Your array is {}".format(binary_array))
temp = int(input("Enter the number you want to search : "))
binary_search(binary_array,temp)