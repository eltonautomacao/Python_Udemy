# Operadores Relacionais == < > >= <= !=
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
idade = int(idade)#cast stringa para int
# Limite para o emprestimo
menor = 20
maior = 30
if idade >= menor and idade <= maior:
    print(f'{nome} pode pegar um emprestimo!')
else:
    print(f'{nome} você não pode pegar o emprestimo!')
