#Em Python, os blocos são definidos pela indentação. 
# Diferente de C e Java, que usam as chaves { e } para delimitar os blocos, em Python, 
# todos os blocos são iniciados com o símbolo : (dois pontos) na linha superior e representados 
# pelo acréscimo de 4 (quatro) espaços à esquerda.

# Inicializa a variável 'a' com o valor zero.
a = 0

# Inicia um loop que irá tentar executar 30 vezes (para i de 0 a 29).
# A variável 'i' é usada apenas para contar as iterações e não afeta o valor de 'a'.
for i in range(30):
    
    # Verifica se o valor atual de 'a' é um número par.
    if a % 2 == 0:
        
        # Se 'a' for par, incrementa 'a' em 1 (tornando-o ímpar).
        a += 1
        
        # 'continue' faz com que o código pule para a próxima iteração do loop 'for' imediatamente, 
        # ignorando o bloco 'else' abaixo.
        continue
    
    # Se 'a' for ímpar (porque o 'if a % 2 == 0' não foi atendido ou o 'continue' não foi executado na última vez):
    else:
        
        # Verifica se o valor atual de 'a' é um múltiplo de 5.
        if a % 5 == 0:
            
            # Se 'a' for ímpar E múltiplo de 5 (ou seja, 5, 15, 25...), 
            # 'break' interrompe o loop 'for' completamente.
            break
        
        # Se 'a' for ímpar E não for múltiplo de 5:
        else:
            
            # Incrementa 'a' em 3.
            a += 3

# Imprime o valor final da variável 'a' após o loop ser concluído (ou interrompido).
print (a)