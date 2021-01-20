"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper()) # deixa tudo em maiusculo

print(nome.lower()) # deixa tudo em minusculo

print(nome.split()) # Trasforma em uma lista de strings

print(nome[0:4])    # Slice de string

print(nome[5:15])   # Slice de string

# [   0  ,      1      ]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])

"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])   # Inversão da String Pythonico

print(nome.replace('G', 'P'))
