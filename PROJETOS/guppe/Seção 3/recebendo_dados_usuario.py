
"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é String

Em python string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples - 'Thalles Fernandes'
- Aspas duplas - "Thalles Fernandes"
- Aspas simples triplas - '''Thalles Fernandes'''
"""
# - Asplas duplas triplas - """Thalles Fernandes"""

# Entrada de dados
# Forma padrão para input
# print('Qual seu nome ?')
# nome = input()

# Forma simplificada
nome = input('Qual seu nome')

# Exemplo de print 'antigo' Python 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' Python 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' Python 3.7
print(f'Seja bem-vindo(a) {nome}')

# Exemplo de print 'antigo' Python 2.x
# print('Qual sua idade %s ?' % nome)

# Exemplo de print 'moderno' Python 3.x
# print('Qual sua idade {0} ?'.format(nome))

# Exemplo de print 'mais atual' Python 3.7
# Forma padrão para input
# print(f'Qual sua idade {nome} ?')
# idade = input()

# Forma simplificada para input
idade = int(input(f'Qual sua idade {nome} ?'))

# Exemplo de print 'antigo' Python 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' Python 3.x
# print('{0} você tem {1} anos! '.format(nome, idade))

# Exemplo de print 'mais atual' Python 3.7
print(f'{nome} você tem {idade} anos!')

"""
int(idade) -> cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2020 - idade}')
