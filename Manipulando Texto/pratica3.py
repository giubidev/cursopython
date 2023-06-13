# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input("Digite uma frase: ")


up = frase.upper()
quant1 = up.count("A")
posic = frase.find("A")
posic1 = frase.rfind("A")

print('''A frase é: {}
Ela possui {} letras "A"
A posição da primeira letra A está em {}
A posição da última letra A está em {}'''.format(frase, quant1, posic, posic1))
