"""

# Ex 1 - Seção 7

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]

print(soma)

A[4] = 100

print(A)

for i in A:
    print(i)


# Ex 2 - Seção 7

cont = 0
lista = []
while cont < 6:
    vlr = int(input())
    lista.append(vlr)
    cont = cont + 1
print(lista)


# Ex 3 - Seção 7

cont = 0
listReal = []
listResult = []

while cont < 10:
    vlr = float(input())
    listReal.append(vlr)
    vlrQuad = vlr ** 2
    listResult.append(vlrQuad)
    cont = cont + 1
print(listReal)
print(listResult)


# Ex 4 - Seção 7

lista = list(range(8))
print(lista)

x = int(input('Informe a primeira posição do vetor para a soma:'))
y = int(input('Informe a segunda posição do vetor para a soma:'))

print(lista[x] + lista[y])


# Ex 5 - Seção 7

lista = []
contPar = 0
cont = 0

while cont < 10:
    vlr = int(input())
    lista.append(vlr)
    if vlr % 2 == 0:
        contPar = contPar + 1
    cont = cont + 1

print(contPar)


# Ex 6 - Seção 7

lista = []
cont = 0

while cont < 10:
    vlr = int(input('informe um valor:'))
    lista.append(vlr)
    cont = cont + 1

print(max(lista))
print(min(lista))


# Ex 7 - Seção 7

lista = []
cont = 0
maxi = 0

while cont < 10:
    vlr = int(input())
    lista.append(vlr)
    cont = cont + 1
print(lista)
maxi = max(lista)
print(maxi)
print(lista.index(maxi))

# Ex 8 - Seção 7

lista = []
cont = 0

while cont < 6:
    vlr = int(input())
    lista.append(vlr)
    cont = cont + 1
print(lista)
print(lista[::-1])


# Ex 9 - Seção 7

lista = []
cont = 0

while cont < 6:
    vlr = int(input())
    if vlr % 2 == 0:
        lista.append(vlr)
        cont = cont + 1
    else:
        print('O valor informado é impár! Por favor informe apenas números pares!')

print(lista)
print(lista[::-1])


# Ex 10 - Seção 7

lista = []
cont = 0

while cont < 15:
    vlr = int(input('Informe a media do aluno:'))
    lista.append(vlr)
    cont = cont + 1
print(lista)

soma = sum(lista)
media = soma / 15
print(media)

"""
