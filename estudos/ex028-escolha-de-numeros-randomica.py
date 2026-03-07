from random import choice, randint
np = int(input('Escolha um número entre 0 a 5.\ntente adivinhar:\n'))
'''lista = ['0','1','2','3','4','5']
escolhido = choice(lista)'''
escolhido = randint(0, 5)
if np == escolhido:
    print(f'O número que pensei foi {escolhido}')
    print(f'Você escolheu {np}')
    print('Prabens você acertou')
else:
    print(f'O número que pensei foi {escolhido}')
    print(f'Você escolheu {np}')
    print('Que pena não foi desta vez...')
print('Ate a proxima')