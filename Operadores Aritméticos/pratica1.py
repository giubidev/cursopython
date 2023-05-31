# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# Solicitar ao usuário para digitar um número
n = int(input("Digite um número inteiro: "))

# Fazendo o antecessor e o sucessor do número digitado pelo usuário
ant = (n - 1)
suc = (n + 1)

# Exibindo na tela os valores
print("O número {}, tem como antecessor o {} e o sucessor {}.".format(n, ant, suc))
