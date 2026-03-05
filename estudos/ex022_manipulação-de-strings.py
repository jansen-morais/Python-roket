nome = str(input('Digite seu nome completo:\n')).strip()
# o comando ".strip()" elimina os espaçoes na string
print(f'''Analisando seu nome...\n
Seu nome em letras maiusculas {nome.upper()}
Seu nome me letras minusculas {nome.lower()}''')
#f'...'-> Formata o texto final inserindo o resultado da contagem dentro da frase
print(f'Seu nome contem a quantidade de {len(nome.split())} palavras')
#nome.split() -> Divide o texto em uma lista, separando por espaços: ['Ana', 'Maria', 'Silva']
#len(...) -> Conta quantos itens existem nessa lista gerada (no caso, 3)
print(f'Seu nome tem a quantidade de {len(nome) - nome.count(" ")} letras')
# aqui eu usei o comando "- nome.count(" "), para retirar os espaçoes da contagem
'''# print(f'Seu primeior nome tem {nome.find(" ")}')
# nome.find(" ") -> Procura a posição do PRIMEIRO espaço em branco na frase.
# Como o Python começa a contar do zero (0), a posição do primeiro espaço
# coincide exatamente com a quantidade de letras do primeiro nome.'''
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
# nome.split() cria uma lista de palavras.
# [0] pega apenas a primeira palavra da lista.
# len(...) conta as letras dessa primeira palavra.
'''primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')
# Divide o nome em uma lista e pega apenas o primeiro item [0], depois conta as letras'''