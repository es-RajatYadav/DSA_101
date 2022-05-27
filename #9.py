def findDuplicate(array):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if i == j:
                continue
            elif array[i] == array[j]:
                return 1
    return 0


if findDuplicate([1, 2, 4, 5, 6]) == 0:
    print('False')
else:
    print('True')
