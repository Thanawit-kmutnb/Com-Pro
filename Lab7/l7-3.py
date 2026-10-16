def transpose_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = arr[i][j]

    return result

data = [[1, 2], [3, 4], [5, 6]]
print(transpose_matrix(data))


