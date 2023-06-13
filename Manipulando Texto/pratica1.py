
## Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúscula
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

gg = nome.upper()
pp = nome.lower()
quant = len(nome)
div = nome.split()
primeiro = len(div[0])

print('''O nome é: {}
Com as letras maiusculas: {}
Com as letras minusculas: {}
Quantidade de letras: {}
Quantidade de letra primeiro nome: {}'''.format(nome, gg, pp, quant, primeiro))
