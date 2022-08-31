"""
Faça um programa que peça ao usuário para digitar un número inteiro ,
informe se este numero é par ou impar. Caso o usuário não digite um numero
 inteiro, informe que não é um número par.
"""
inteiro = input('Digite um número. ')
if inteiro.isdigit():
    inteiro = int(inteiro)
    if inteiro % 2 == 0:
        print(f'{inteiro} é par')
    else:
        print(f'{inteiro} é ímpar')
else:
    print('Isso não é um número.')