tabla = [
    ['X', 'O', None],
    [None, 'X', 'O'],
    ['O', None, 'X']
]

for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        if tabla[i][j] == None:
            tabla[i][j] = '_'


for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        if tabla[i][j] == '_' and i == 0 and j == 2:
            tabla[i][j] == 'O'
for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        print(tabla[i][j], end=' ')
    print()
