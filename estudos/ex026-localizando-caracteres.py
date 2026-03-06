# Solicita a frase, padroniza para minúsculas, remove espaços das pontas e do meio
frase = str(input('Digite uma frase:\n')).lower().strip().replace(" ", "")
# Conta quantas vezes o caractere "a" aparece na string limpa
print(f'A letra "A" aparece {frase.count("a")} vezes.')
# Encontra o índice da primeira ocorrência. Somamos 1 pois o Python inicia a contagem em 0
print(f'A primeira letra "A" aparece na posição {frase.find("a") + 1}')
# Encontra o índice da última ocorrência (começando da direita para a esquerda)
print(f'A última letra "A" aparece na posição {frase.rfind("a") + 1}')
# Exibe o tamanho total da frase após a remoção de todos os espaços
print(f'A frase tem {len(frase)} letras.')