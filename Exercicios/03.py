""""
Faça um programa que peça o primeiro nome do usuario.
Se ele tiver 4 letras escreva "Seu nome é curto"
Se ele tiver entr 5 e 6 letras escreva "Seu nome e normal",
se maior escreva "Seu nome é grande."
"""
nome = input('Digite seu nome. ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <=6:
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')