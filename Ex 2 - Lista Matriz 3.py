matriza  = [[1, 2], [4, -1]]
matrizai  = [[0, 0], [0, 0]]
ad =  0


print()
print('Matriz A')
print('=-'* 5)
for j in matriza:
    print(j)
print('=-'* 5)
print()

def det2(matriza):
    return matriza[0][0]*matriza[1][1] - matriza[0][1]*matriza[1][0]

def inv2(matriz):
    d = det2(matriza)
    return [[matriza[1][1]/d, -matriza[0][1]/d], [-matriza[1][0]/d, matriza[0][0]/d]]

matrizai = inv2(matriza)
ad = det2(matriza)

if(ad==9 or ad==-9):
    print('=-' * 18)
    print('A Matriz inversa de A é igual a 1/9A')
    print('=-' * 18)
    print()
else:
    print('=-' * 18)
    print('A Matriz inversa de A NÃO é igual a 1/9A')
    print('=-' * 18)
    print()

print('Matriz A Inversa:')
print('=-'* 8)
for l in  range (2):
    for c in range(2):
        print(f'[{matrizai[l][c]:^5.2f}]', end='')
    print()
print('=-'* 8)