""""
 Faça um programa que pergunte a hora ao usuário, baseando-se
 no horário descrito, exiba a saudação apropriada. Ex bom dia 0-11,
 Boa tarde 12-17, Boa noite 18-23.
"""
hora = input('Digite um horário.')
if hora .isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horario deve estar entre 0 á 23. ')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')