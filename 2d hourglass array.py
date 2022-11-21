def hourglassSum(arr):
    # constraint of min -9 x 7
    maxSum = -63
    for row in range(0,4):
        for col in range(0,4):
            currSum = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if currSum > maxSum:
                maxSum = currSum
    return maxSum
