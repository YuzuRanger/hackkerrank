    swaps = 0
    for currIndex in range(len(arr)):
        print('current index: ', currIndex)
        while arr[currIndex] != currIndex + 1:
            # when value of current item a[3] is 1, should be 4, find index of val 4
            newIndex = arr[currIndex] - 1
            print("desired index: ", newIndex)

            # my_list[indexOf],my_list[indexOf+1] = my_list[indexOf+1],my_list[indexOf]
            arr[currIndex], arr[newIndex] = arr[newIndex], arr[currIndex]
            swaps += 1
    return swaps
