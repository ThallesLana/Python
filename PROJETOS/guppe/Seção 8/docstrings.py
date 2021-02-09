"""
Documentando funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python
utilizando a propriedade __doc__

Podemos ainda fazer acesso á documentação com a função help()
"""

print(help(print))

# Exemplos


def diz_oi():
    """ Uma função simples que retorna a string 'Oi!' """
    return 'Oi!'


def exponecial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'Potencia'
    """
    return numero ** potencia
