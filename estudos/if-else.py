from time import sleep
import sys



def mde(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.07)
    print()
# comando que faz as strings serem imprimidas como numa maqina de escrever 
mde(f'Digite a primeira nota:')
n1 = float(input())
sleep(1.0)
mde(f'Digite a segunda nota:')
n2 = float(input())
sleep(1.0)
m = (n1+n2)/2
mde(f'Sua media foi {m:.1f}')
sleep(0.7)
if m > 6.0:
    mde(f'Sua media está boa')
    sleep(0.7)
    mde('Continue assim')
    sleep(0.7)
else:
    mde(f'Sua media esta ruim!')
    sleep(0.7)
    mde('precisa estudar mais')
    sleep(0.7)
mde('Ate a proxima\n:)')
sleep(2.0)