palavra = input("Digite uma palavra: ")
palavInvertida = ""
for i in range(len(palavra)-1, -1, -1):
    palavInvertida += palavra[i]
print(f"Palavra invertida: {palavInvertida}")