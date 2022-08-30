"""
Operadores logicos
And, Or, not, in e not in

nome = 'elton'
if 'el'not in nome:
    print('Executei')
else:
    print('Existe no texto')
"""
usuario = input('Nome de usuario ')
senha = input('Senha do usuario ')

usuario_bd = 'Elton'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Bem vindo')
else:
    print('Usuario e senha invalidos')