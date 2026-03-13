def main():# Aqui inicia a função principal 
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []# Aqui será a variável que vai armazenar as entradas em formato de lista
    
    while True:# Esta é a função de loop que roda até ser interrompida
        entrada = input(">")# Esta variável capta as entradas de texto do teclado
        if entrada.lower() == "sair":# Aqui será uma condição para finalizar o loop (converte para minúsculo para evitar erro)
            break# Para o programa caso a condição seja alcançada
        frases.append(entrada)# Aqui com o "append" tudo que entrar será colocado no final da lista sem que nada seja apagado 
    
    # O comando "with" serve para fechar o arquivo aberto após o bloco finalizar seu trabalho 
    with open("meu_arquivo.txt","w+", encoding= 'utf-8') as arquivo:# Aqui abre-se o arquivo com a função de escrita "w+" que permite ler e escrever (sobrescreve o anterior)
        for frase in frases:# Aqui o "for" percorre cada item da lista "frases" para processar um por um
            arquivo.write(frase + "\n")# Aqui escreve as entradas quebrando a linha após a finalização da escrita 
    # para que eu abra o arquivo sem apagar os textos antigos preciso usar o "a","append" para gravar e não sobrepor os que já estão la        
    print("Arquivo original criado. Agora vamos manipular os dados.")
    
    dados_modificados = []# Aqui cria a lista para receber as strings que serão transformadas
    
    with open("meu_arquivo.txt","r", encoding= 'utf-8') as arquivo:# Aqui abro o meu arquivo no modo leitura com o "r" (apenas ler)
        for linha in arquivo:# Aqui o "for" lê o arquivo linha por linha automaticamente
            # O "strip" remove espaços/quebras de linha e o "upper" deixa tudo em MAIÚSCULO
            dados_modificados.append(linha.strip().upper())# Aqui adiciona a frase já modificada na nova lista retirando os espaços sobressalentes e conertendo em maiusculas
    #O encoding= 'utf-8' traduz oa caracteres especiais no caso de windows        
    with open("meu_arquivo.txt", "w+", encoding= 'utf-8') as arquivo:# Aqui abre o arquivo novamente no modo "w" para limpar o antigo e gravar o novo
        for linha in dados_modificados:# Aqui o "for" percorre a lista de dados já transformados
            arquivo.write(linha + "\n")# Aqui grava a linha modificada de volta no arquivo físico
            
    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__=="__main__":# Esta condição verifica se o script está sendo executado diretamente
    main()# Aqui faz a chamada da função para o programa começar a rodar

    '''lembrando que eu posso usar alguns comandos para ller a slinhas do arquivo cmo "read, readline, readlines"
    sendo que cada um vai tomar e leuma parte difernte.
    a unica exeção sento o "readline", que le a primeira linhae fica parado ali e caso eu chame esta função novente
     ele kera a sengunda linha.
      já o read lera e me aprensantara tudo como se fosse uma striing só.'''