from time import sleep 
import sys
def mde(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.05)
    print()

mde('Digite seu nome completo:')
n = str(input()).strip()
sleep(1.5)
nome = n.split()# essa comando transforma em lista a string
mde(f'Muito prazer em te conhecer!')
sleep(1.5)
mde(f'seu primeiro nome é {nome[0]}')
sleep(1.5)
mde(f'E seu ultimo nome é {nome[-1]}')