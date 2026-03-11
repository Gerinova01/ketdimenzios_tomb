matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[2][1])
for sor in matrix:
    print(sor)
    # for oszlop in sor:
    #     print(oszlop, end=" ")


# csak szabályos 3*3 5*5
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        print(matrix[i][j], end= " ")