# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: 6.127 -> 6

# Importando a biblioteca math
import math

# Solicitando o numero para o usuário
numreal = float(input("Digite um número real: "))

# Truncando o número para ficar apenas a parte inteira
trunc = math.trunc(numreal)

# Exibir para o usuário a parte inteira do número
print("A parte inteira do número real é: {}".format(trunc))
