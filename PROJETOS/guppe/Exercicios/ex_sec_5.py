"""
# Ex 1 - Seção 5
n1 = 9
n2 = 9

if n1 > n2:
    print('Numero 1 é maior')
elif n1 < n2:
    print('Numero 2 é maior')
else:
    print('Os numeros 1 e 2 são iguais')

# Ex 2 - Seção 5
n1 = float(input('Digite um valor'))

if n1 > 0:
    r2 = n1 ** (1/2)
    print(r2)
else:
    print('O número informado é invalido')

# Ex 3 - Seção 5
n1 = -400.0

if n1 > 0:
    r2 = n1 ** (1 / 2)
    print(r2)
else:
    q2 = n1 ** 2
    print(q2)

# Ex 4 - Seção 5
n1 = 4

if n1 > 0:
    q1 = n1 ** 2
    r1 = n1 ** (1 / 2)
    print(q1)
    print(r1)
else:
    print('Número negativo é invalido!')

# Ex 5 - Seção 5
n1 = 4

if n1 % 2 == 0:
    print('Número é par!')
else:
    print('Número é impár!')

# Ex 6 - Seção 5
n1 = 20
n2 = 20

if n1 > n2:
    maior = n1
    result = maior - n2
    print('Numero 1 é o maior')
    print(f'A diferença entre eles é de: {result}')
elif n2 > n1:
    maior = n2
    result = maior - n1
    print('Numero 2 é o maior')
    print(f'A diferença entre eles é de: {result}')
else:
    print('Os numeros são iguais')

# Ex 7 - Seção 5
n1 = 200
n2 = 200

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print('Os numeros são iguais')

# Ex 8 - Seção 5
nota1 = float(input('Informe a primeira nota do aluno: \n'))
nota2 = float(input('Informe a segunda nota do aluno: \n'))

if nota1 > 0.0 < 10.0:
    media = nota1
    if nota2 > 0.0 < 10.0:
        media = media + nota2
        result = media / 2
    print(f'As notas do aluno são validas, sua media do bimestre foi: {result}')
else:
    print('Notas informadas são invalidas!')


# Ex 9 - Seção 5
salario = float(input('Informe seu salario:'))
emprestimo = float(input('Informe o valor da prestação do emprestimo:'))

vinteP = salario * 0.2

if emprestimo > vinteP:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')

# Ex 10 - Seção 5

h = float(input('Informe sua altura:'))
s = input('Informe o sexo: (M/F)')

if s == 'M' or 'm':
    pi = (72.7 * h) - 58
    print(f'Seu peso ideal é: {pi}')
elif s == 'F' or 'f':
    pi = (62.1 * h) - 44.7
    print(f'Seu peso ideal é: {pi}')

"""

