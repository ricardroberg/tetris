# MATRIZ PRINCIPAL
matriz = [[0,  1,   2,  3],
          [4,  5,   6,  7],
          [8,  9,  10, 11],
          [12, 13, 14, 15]]

# NÃO CONSEGUI FAZER PELO DICIONÁRIO A REPOSIÇÃO DE NÚMEROS DA MATRIZ PRINCIPAL PELOS SIMBOLOS DO TETROMINIO
tetrominio1 = [{0: ' ',  1:' ',   2:'X',  3:' '},
                {4:' ',  5:' ',   6:'X',  7:' '},
                {8:' ',  9:'X',  10:'X', 11:' '},
                {12:' ', 13:' ', 14:' ', 15:' '}]

# FIZ PELA LISTA
t1 = [' ', ' ', ' ', ' ',
      ' ', ' ', ' ', ' ',
      ' ', ' ', 'X', 'X',
      ' ', ' ', 'X', 'X']

t2 = [' ', ' ', 'X', ' ',
      ' ', ' ', 'X', ' ',
      ' ', 'X', 'X', ' ',
      ' ', ' ', ' ', ' ']

t3 = [' ', 'X', ' ', ' ',
      ' ', 'X', ' ', ' ',
      ' ', 'X', 'X', ' ',
      ' ', ' ', ' ', ' ']

t4 = [' ', ' ', 'X', ' ',
      ' ', ' ', 'X', ' ',
      ' ', ' ', 'X', ' ',
      ' ', ' ', 'X', ' ']

t5 = [' ', 'X', ' ', ' ',
      ' ', 'X', 'X', ' ',
      ' ', ' ', 'X', ' ',
      ' ', ' ', ' ', ' ']

t6 = [' ', ' ', 'X', ' ',
      ' ', 'X', 'X', ' ',
      ' ', 'X', ' ', ' ',
      ' ', ' ', ' ', ' ']

t7 = [' ', ' ', ' ', ' ',
      ' ', 'X', ' ', ' ',
      'X', 'X', 'X', ' ',
      ' ', ' ', ' ', ' ']

matriztemp0 = [[], [], [], []]
matriztemp90 = [[], [], [], []]
matriztemp180 = [[], [], [], []]
matriztemp270 = [[], [], [], []]

for n in range(16):
    for x, i in enumerate(matriz):
        if n in i:
            w = len(i)
            y = i.index(n)
            #print(f'Valor = {n}, X = {y}, Y = {x}')
            matriztemp0[i.index(n)].insert(x, t2[(y * w + x)])
            matriztemp90[i.index(n)].insert(x, t2[(12 + y - (x * w))])
            matriztemp180[i.index(n)].insert(x, t2[(15 - (y * w) - x)])
            matriztemp270[i.index(n)].insert(x, t2[(3 - y + (x * w))])



for i in matriztemp0:
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