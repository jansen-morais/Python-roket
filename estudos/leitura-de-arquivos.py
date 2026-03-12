import os  # Importa a biblioteca 'Operating System', necessária para manipular caminhos de pastas e arquivos.

# Abre o arquivo 'dados1.txt'. 
# "w" (write): Modo de escrita (cria o arquivo ou sobrescreve se já existir).
# encoding='utf-8': Define o padrão de caracteres para aceitar acentos (como o 'á').
arquivo1 = open('dados1.txt', "w+", encoding='utf-8')

# Escreve a string "ola mundo!!" dentro do arquivo aberto.
arquivo1.write("ola mundo!!") 
arquivo1.write('\nAcreção de texto.')
'''arquivo1.write(input())'''

# Aqui eu acrecento um um comando onde eu grovo no "arquivo" a partir do pronpt
entrda=input('digite algo que queira gravar no arquivo:\n')
arquivo1.write(f'\n{entrda}')

# arquivo1.closed: Atributo que retorna True se o arquivo estiver fechado e False se estiver aberto.
print('O arquivo foi fechado?', arquivo1.closed)

# os.path.relpath: Retorna o caminho "relativo" (a partir da pasta onde você está agora).
real = os.path.relpath('dados1.txt')

# os.path.abspath: Retorna o caminho "absoluto" completo (desde a partição C: ou Root /).
abs = os.path.abspath('dados1.txt')

print('Caminho relativo do arquivo', real)
print('Caminho absoluto do arquivo', abs)
print('--'*20)
# ... depois de todos os seus writes ...
arquivo1.seek(0) # Volta para o início do arquivo
conteudo = arquivo1.read()
print('tipo de conteudo',type(conteudo))
print('conteudo retornado pelo Read:')
print(repr(conteudo))

# arquivo1.name: Pega o nome do arquivo que foi definido na abertura.
print('O nome do arquivo é', os.path.relpath(arquivo1.name))

# arquivo1.mode: Retorna o modo em que o arquivo foi aberto (neste caso, 'w').
print('mode de abertura', arquivo1.mode)

# Imprime o objeto 'arquivo1', que mostra um resumo: nome, modo e codificação.
print(arquivo1)

# Fecha a conexão entre o Python e o arquivo no sistema. Libera o arquivo para ser usado por outros programas.
arquivo1.close()

# Verifica novamente se o arquivo foi fechado (agora deve retornar True).
print('O arquivo foi fechado?', arquivo1.closed)