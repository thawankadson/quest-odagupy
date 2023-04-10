texto = "Hello, world!"

# Invertendo a string
invertido = ""
for i in range(len(texto)-1, -1, -1):
    invertido += texto[i]

# Exibindo o resultado
print(invertido)