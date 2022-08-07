def find_target(matrix, target):
    i = 0
    j = len(matrix) - 1
    while matrix[i][j] != target:
        if i >= len(matrix) or j < 0:
            return [-1, -1]
        if matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return [i, j]


matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]


print(find_target(matrix,44))