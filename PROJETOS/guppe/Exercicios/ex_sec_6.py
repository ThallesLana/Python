"""
# Ex 1 - Seção 6
for num in range(0, 15, 3):
    print(num)


# Ex 2 - Seção 6
frnum = 1

for frnum in range(1, 101, 1):
    print(frnum)

whnum = 0

while whnum < 100:
    whnum = whnum + 1
    print(whnum)

donum = 0

while True:
    if donum == 100:
        break
    else:
        donum = donum + 1
        print(donum)
print('Cabo o lol')


# Ex 3 - Seção 6
num = 11
while True:
    if num == 0:
        break
    else:
        num = num - 1
        print(num)
print('Fim!')

# Ex 4 - Seção 6
for num in range(0, 101000, 1000):
    print(num)


# Ex 5 - Seção 6

result = 0
cont = 0

while cont < 10:
    num = int(input('Informe um valor: '))
    result = result + num
    cont = cont + 1
print(result)


# Ex 6 - Seção 6

result = 0
cont = 0

while cont < 10:
    num = int(input('Informe um valor: '))
    result = result + num
    cont = cont + 1
media = result / 10
print(f'Resultado da soma dos 10 valores foi: {result}')
print(f'Resultado da media dos 10 valores foi: {media}')


# Ex 7 - Seção 6

result = 0
cont = 0

while cont < 10:
    num = int(input('Informe um valor: '))
    if num > 0:
        result = result + num
        cont = cont + 1
    else:
        cont = cont + 1
media = result / 10
print(f'Resultado da soma dos 10 valores foi: {result}')
print(f'Resultado da media dos 10 valores foi: {media}')


# Ex 8 - Seção 6

result = 0
cont = 0
maior = 0
menor = 1000

while cont < 10:
    num = int(input('Informe um valor: '))
    if num > maior:
        maior = num
        cont = cont + 1
    elif num < menor:
        menor = num
        cont = cont + 1

print(f'O menor numero registrado foi: {menor}')
print(f'O maior numero registrado foi: {maior}')


# Ex 9 - Seção 6

num = int(input('Informe o numero impar que deseja iniciar: '))
qts = int(input('Informe quantos numeros impares naturais deseja ver a frente deste:'))
cont = 0

while cont < qts:
    if num % 2 == 1:
        num = num + 2
        print(num)
        cont = cont + 1
    else:
        print('O numero informado é par! Programa Encerrado!')
        break

# Ex 10 - Seção 6

cont = 0
soma = 0

while cont <= 100:
    if cont % 2 == 0:
        soma = soma + cont
        cont = cont + 1
    else:
        cont = cont + 1
print(f'A soma de todos os valores pares é: {soma}')

"""

