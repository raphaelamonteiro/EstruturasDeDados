# Seja uma lista de inteiros, mostre apenas os números pares
#usando list comprehension.

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [inteiro for inteiro in inteiros if inteiro % 2 ==0]

print(pares)
