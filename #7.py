def findMaxSubArray(array):
    Max = array[0]
    cur_max = 0
    for i in array:
        cur_max += i
        if cur_max < 0:
            cur_max = 0

        elif Max < cur_max:
            Max = cur_max

    print(Max)


findMaxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
