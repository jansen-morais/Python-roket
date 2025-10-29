class Fatorial:
    """
    Classe responsável por calcular o fatorial de um número inteiro não negativo.
    Utiliza uma abordagem de recursão para realizar o cálculo.
    """

    def calcular(self, n):
        """
        Método que calcula o fatorial de um número 'n'.

        O cálculo é feito de forma recursiva: n! = n * (n-1)!.

        Args:
            n (int): O número inteiro não negativo para o qual o fatorial será calculado.

        Returns:
            int: O valor do fatorial de 'n'.
        """
        
        # Caso base da recursão: 0! é igual a 1
        if n == 0:
            return 1
        
        # Passo recursivo: n * (fatorial de n-1)
        else:
            return n * self.calcular(n - 1)

# --- Execução do Código ---

# 1. Criação de uma instância da classe Fatorial
f = Fatorial()

# 2. Chamada do método calcular e exibição do resultado
# O fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120
print("Fatorial de 5 (orientado a objetos com recursão):", f.calcular(5))