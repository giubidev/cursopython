# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# Solicitando as notas para o usuário
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

# Calculando a média
media = (nota1 + nota2) / 2

# Mostrando na tela a média
print("A média das notas {} e {}, é {}.".format(nota1, nota2, media))
