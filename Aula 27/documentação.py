"""
Documentação, funções :
isnumeric, isdigit, isnumeric
numeros e positivos
"""
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print(n1+n2)
else:
    print('Não posso realizar a operação.')