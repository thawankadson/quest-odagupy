# Definindo o número a ser verificado
num = 21

# Iniciando a sequência com 0 e 1

fib = [0, 1]

# Gerando a sequência até o valor máximo desejado
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

# Verificando se o número pertence à sequência
if num in fib:
    print(f"{num} pertence à sequência de Fibonacci")
else:
    print(f"{num} não pertence à sequência de Fibonacci")   