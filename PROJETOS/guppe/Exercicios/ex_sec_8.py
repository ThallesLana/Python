"""

# Ex 1 - Seção 8

def devolvendo(inteiro):
    return inteiro * 2
    
print(devolvendo(8))


# Ex 2 - Seção 8

def data(dia, mes, ano):
    if mes == 1:
        mesExtenso = 'Janeiro'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 2:
        mesExtenso = 'Fevereiro'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 3:
        mesExtenso = 'Março'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 4:
        mesExtenso = 'Abril'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 5:
        mesExtenso = 'Maio'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 6:
        mesExtenso = 'Junho'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 7:
        mesExtenso = 'Julho'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 8:
        mesExtenso = 'Agosto'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 9:
        mesExtenso = 'Setembro'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 10:
        mesExtenso = 'Outubro'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 11:
        mesExtenso = 'Novembro'
        return f'{dia} de {mesExtenso} de {ano}'
    elif mes == 2:
        mesExtenso = 'Dezembro'
        return f'{dia} de {mesExtenso} de {ano}'

print(data(1, 5, 2001))


# Ex 3 - Seção 8

def verifica(valor):
    if valor == 0:
        return 'Valor informado: igual a 0'
    elif valor > 0:
        return 'Valor informado: Positivo'
    elif valor < 0:
        return 'Valor informado: Negativo'

print(verifica(1))
print(verifica(-3))
print(verifica(0))

# Ex 4 - Seção 8

def perfect(num):
    raizQ = num ** (1/2)
    if ((raizQ ** 2) == num):
        return 'O numero verificado é um quadrado perfeito'
    else:
        return 'O numero verificado não é um quadrado perfeito'

print(perfect(1))

# Ex 5 - Seção 8

def raio(R):
    V = 4/3 * 3.14 * R ** 3
    return V

print(raio(12))


# Ex 6 - Seção 8

def hora(H = 0, M = 0, S = 0):
    if H != 0:
        sH = H * 3600
        sM = M * 60

        horaS = sH + sM + S
        text  = f'O horario informado convertido da: {horaS} segundos!' 
        return horaS
    
    elif M != 0:
        sM = M * 60

        horaS = H + sM + S
        text  = f'O horario informado convertido da: {horaS} segundos!'
        return horaS

    else:
        sS = H + M + S
        text  = f'O horario informado convertido da: {sS} segundos!'
        return sS

print(hora(1, 22, 20))
print(hora(0, 50, 32))
print(hora(0, 0, 52))


# Ex 7 - Seção 8

def Fc(C):
    F = C * (9.0/5.0) + 32.0 
    return F

print(Fc(32))


# Ex 8 - Seção 8

def catetodaporradahipotenusa(a, b):
    Q = (a ** 2) + (b ** 2)
    H = Q ** (1/2)

    return H

print(catetodaporradahipotenusa(2, 4))


# Ex 9 - Seção 8
def cilindro(A, R):
    V = 3.14 * (R ** 2) * A
    return V

print(cilindro(10, 23))

# Ex 10 - Seção 8

def maior(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'são iguais'

print(maior(1, 2))
print(maior(3, 2))
print(maior(2, 2))
print(maior(1, 2))
"""



