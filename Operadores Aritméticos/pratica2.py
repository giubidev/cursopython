# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz

# Solicitando número ao usuário
n = int(input("Digite um número: "))

# Dobro do número
dobro = (n * 2)

# Triplo do número
triplo = (n * 3)

# Raiz quadrada
raiz = n ** (1/2)

# Exibindo os valores para o usuário
print("O número {}, tem como dobro o {}, triplo {} e raiz quadrada {}.".format(n, dobro, triplo, raiz))
