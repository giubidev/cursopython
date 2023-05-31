# Faça um programa que leia um ângulo qualquer e mostre na rela o valor
# do seno, cosseno e tangente desse ângulo.

# Importando a biblioteca
import math

# Solicitando o ângulo para o usuário
ang = int(input("Digite o valor do ângulo: "))

# Calculando o valor do cosseno, seno e tangente
cos = math.cos(ang)
tag = math.tan(ang)
sen = math.sin(ang)

# Exibindo os valores para o usuário
print("Para o ângulo {}, temos: ".format(ang))
print("Seno: {}".format(sen))
print("Cosseno: {}".format(cos))
print("Tangente: {}".format(tag))
