import os
import shutil

def porcecessar_arquivo(arquivo_origem, arquivo_destino):
    try:#comoando para tentar execultar as intruções 
        with open(arquivo_origem, 'r', encoding='utf8') as f_origem:
            conteudo = f_origem.read()
    #comando parao caso de exeções 
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem}, não encontrado.')        
        return
    except PermissionError:
        print(f'Sem perção para ler o {arquivo_origem}.')
        return
    except Exception as e:
        print(f'Erro inesperado ao ler {arquivo_origem}: {e}')
        return
    
    try:
        with open(arquivo_destino, 'w+', encoding='utf8') as f_destino:
            f_destino.write("Cabeçalho: conteudo do Arquivo\n")
            f_destino.write(conteudo) 
    except PermissionError:
        print(f'Sem permição para eccrever em {arquivo_destino}')
    except Exception as e:
        print(f'Erro inesperado ao escrever em {arquivo_destino}: {e}')

def main():
    diretorio_trabalho = "diretorio_trabalho"
    arquivo_origem = os.path.join(diretorio_trabalho, "arquivo_origem.txt")
    arquivo_destino = os.path.join(diretorio_trabalho, "arquivo_destino.txt")

    porcecessar_arquivo(arquivo_origem, arquivo_destino)
 

if __name__ == "__main__":
    main()