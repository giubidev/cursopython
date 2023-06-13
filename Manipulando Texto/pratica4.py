# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = input("DIgite seu nome completo: ")

dividir2 = nome.rsplit()
primeiro = dividir2[0]
ultimo = dividir2[-1]

print('''O nome da pessoa é {}
O primeiro nome é {}
O último nome é {} '''.format(nome, primeiro, ultimo))
