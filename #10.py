def rotateArray(array, times):
    for i in range(times):
        temp = array.pop()
        array.insert(0, temp)

    return array


times = int(input('Enter k : '))
print(rotateArray([1, 2, 3, 4, 5, 6], times))
