def alterZeros(array):
    numOfZeros = 0
    n = len(array)
    i = 0
    while i < n:
        if array[i] == 0:
            numOfZeros += 1
            del array[i]
            n -= 1
        else:
            i += 1

    for i in range(numOfZeros):
        array.append(0)

    print(array)


alterZeros([1, 0, 2, 0, 0, 3, 1])
