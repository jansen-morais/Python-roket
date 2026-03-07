from random import choice
#import random 
a1 = input('Peimeiro aluno:\n')
a2 = input('Segundo aluno:\n')
a3 = input('Terceiro aluno:\n')
a4 = input('Quarto aluno:\n')
lista = [a1, a2, a3, a4] #para criar uma lista vc precisa por entre chaves
escolhido = choice(lista)
#escolhido = random.choice(lista)
print(f'O aluno esoclido foi {escolhido}')