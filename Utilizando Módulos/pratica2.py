# Faça um programa que eia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Solicitando ao usuário o valor dos catetos
cata = int(input("Digite o cateto adjacente: "))
cato = int(input("Digite o cateto oposto: "))

# Calculando a hipotenusa
hip = (cata ** 2) + (cato ** 2)

# Exibindo o valor da hipotenusa para o usuário
print("O comprimento da hipotenusa é {}".format(hip))
