"""
-------------------------
\  0  \  1  \  2  \  3  \
\  4  \  5  \  6  \  7  \
\  8  \  9  \  10 \  11 \
\  12 \  13 \  14 \  15 \
-------------------------
Tetromino 1
0 0 x 0
0 0 x 0
0 x x 0
0 0 0 0


"""
matriz = [[0,  1,   2,  3],
          [4,  5,   6,  7],
          [8,  9,  10, 11],
          [12, 13, 14, 15]]

tetrominio1 = {{0: ' ',  1:' ',   2:'X',  3:' '},
                {4:' ',  5:' ',   6:'X',  7:' '},
                {8:' ',  9:'X',  10:'X', 11:' '},
                {12:' ', 13:' ', 14:' ', 15:' '}}

matriztemp90 = [[], [], [], []]
matriztemp180 = [[], [], [], []]
matriztemp270 = [[], [], [], []]


def rada_noventa(tetromino, degrees):
    matriztemp0 = [[], [], [], []]
    matriztemp90 = [[], [], [], []]
    matriztemp180 = [[], [], [], []]
    matriztemp270 = [[], [], [], []]
    """ Rotate to 90 degrees position"""
    for n in range(16):
        for x, i in enumerate(matriz):
            if n in i:
                y = i.index(n)
                print(f'Valor = {n}, X = {y}, Y = {x}')
                if degrees == 90:
                    matriztemp90[i.index(n)].insert(x, (12 + y - (x * 4)))
                elif degrees == 180:
                    matriztemp180[i.index(n)].insert(x, (15 - (y * 4) - x))
                elif degrees == 270:
                    matriztemp270[i.index(n)].insert(x, (3 - y + (x * w)))

# RODA 90, 180, 270
# POSIÇÃO 0 SERIA MATRIZ ORIGINAL

for n in range(16):  # TAMANHO TOTAL DA MATRIZ
    for x, i in enumerate(matriz):
        if n in i:
            w = len(i)
            y = i.index(n)
            print(f'Valor = {n}, X = {y}, Y = {x}')
            matriztemp90[i.index(n)].insert(x, (12 + y - (x * w)))  # VALORES 12, 15 E 3
            matriztemp180[i.index(n)].insert(x, (15 - (y * w) - x))  # SE REFEREM AOS
            matriztemp270[i.index(n)].insert(x, (3 - y + (x * w)))  # CANTOS DA MATRIZ

for i in matriz:
    print(i)
print()
for i in matriztemp90:
    print(i)
print()
for i in matriztemp180:
    print(i)
print()
for i in matriztemp270:
    print(i)

















# matriz2 = [[0,  1,  2],
#           [3,  4,   5],
#           [6,  7,  8]]
#
# matriztemp90 = [[], [], []]
# matriztemp180 = [[], [], []]
# matriztemp270 = [[], [], []]
#
#
# for n in range(9):  # TAMANHO TOTAL DA MATRIZ
#     for x, i in enumerate(matriz2):
#         if n in i:
#             w = len(i)
#             y = i.index(n)
#             print(f'Valor = {n}, X = {y}, Y = {x}')
#             matriztemp90[i.index(n)].insert(x, (6 + y - (x * w)))  # VALORES 6, 8 E 2
#             matriztemp180[i.index(n)].insert(x, (8 - (y * w) - x))  # SE REFEREM AOS
#             matriztemp270[i.index(n)].insert(x, (2 - y + (x * w)))  # CANTOS DA MATRIZ
#
# for i in matriz2:
#     print(i)
# print()
# for i in matriztemp90:
#     print(i)
# print()
# for i in matriztemp180:
#     print(i)
# print()
# for i in matriztemp270:
#     print(i)