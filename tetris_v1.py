
def roda(tetrominio, angulo):
    global matriztemp
    matriztemp = [[], [], [], []]
    for n in range(16):
        for x, i in enumerate(matriz):
            if n in i:
                w = len(i)
                y = i.index(n)
                if angulo == 0:
                    matriztemp[i.index(n)].insert(x, tetrominio[(y * w + x)])
                if angulo == 90:
                    matriztemp[i.index(n)].insert(x, tetrominio[(12 + y - (x * w))])
                if angulo == 180:
                    matriztemp[i.index(n)].insert(x, tetrominio[(15 - (y * w) - x)])
                if angulo == 270:
                    matriztemp[i.index(n)].insert(x, tetrominio[(3 - y + (x * w))])
    return matriztemp

# MATRIZ PRINCIPAL
global matriz

matriz = [[0,  1,   2,  3],
          [4,  5,   6,  7],
          [8,  9,  10, 11],
          [12, 13, 14, 15]]

#matriztemp = [[], [], [], []]

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

while True:
    t = input('Escolha o Tetromínio (t1 a t7): ')
    if t not in ['t1', 't2', 't3', 't4', 't5', 't6', 't7']:
        print('VALOR INCORRETO!')
        break
    a = int(input('Digite o  ângulo(0, 90, 180, 270): '))
    if a not in [0, 90, 180, 270]:
        print('VALOR INCORRETO!')
        break
    ttemp = eval(t)
    roda(ttemp, a)
    for i in matriztemp:
        print(i)
    print()