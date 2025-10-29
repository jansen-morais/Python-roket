class fatorial:
    def cauculadora (self, n):
        if n == 0:
            return 1
        else:
            return n * self.calcular (n-1)
f=fatorial ()
print("fatorial de 5 (orientado a objetos):", f.caucular (5))