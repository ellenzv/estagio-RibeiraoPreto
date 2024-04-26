valor = int(input("Digite um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < valor:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if valor in fibonacci:
    print(f"O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"O número {valor} não pertence à sequência de Fibonacci.")

print(f"Sequência de Fibonacci até o número: {fibonacci}")