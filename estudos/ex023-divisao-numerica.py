num = int(input('Digite um número:\n'))

# O cálculo abaixo usa:
# // (Divisão Inteira): Remove as casas decimais que não interessam no momento.
# %  (Módulo/Resto): Pega o resto da divisão por 10, que isola o último dígito.

u = num // 1 % 10    # Pega o número, divide por 1 e isola o último dígito (Unidade)
d = num // 10 % 10   # Move a vírgula 1 casa para a esquerda e isola o dígito (Dezena)
c = num // 100 % 10  # Move a vírgula 2 casas para a esquerda e isola o dígito (Centena)
m = num // 1000 % 10 # Move a vírgula 3 casas para a esquerda e isola o dígito (Milhar)

# Exibe os resultados usando f-strings para formatar a saída
print(f'Analisando o número {num}')
print(f'A unidade é {u}')
print(f'A Dezena é {d}')
print(f'A Centena é {c}')
print(f'A Milhar é {m}')