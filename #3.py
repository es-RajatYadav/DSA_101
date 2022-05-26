# Find duplicate element in an array and calculate the sum of the identical house numzzzzzz
def searchDuplicate(array1):
    tempSum = 0
    hashTable = {}
    for ele in array1:
        if ele in hashTable:
            hashTable[ele] += 1
        else:
            hashTable[ele] = 1

    for item in hashTable:
        if hashTable[item] > 1:
            tempSum += int(item)

    print(tempSum)


try:
    deliveryHome = input()
    deliveryArray = list(deliveryHome)
    searchDuplicate(deliveryArray)

except EOFError as e:
    print("Error")
