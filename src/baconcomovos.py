"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5
    Bacon com ovos
3 - Saber se o número é múltiplo de 3 somente:
    Bacon
4 - Saber se o número é múltiplo de 5 somente:
    Ovos
5 - Saber se o número não é multiplo de 3 e 5
    passa fome
"""
def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'