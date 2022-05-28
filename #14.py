def findSubArrayZero(array):
    total = 0
    hashTable = {
        0: 0
    }

    for i in array:
        total += i
        if total in hashTable:
            return True
        else:
            hashTable[total] = array.index(i)

    return False


if findSubArrayZero([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]):
    print("Sub Array Exists")
else:
    print("Sub Array Not found.")
