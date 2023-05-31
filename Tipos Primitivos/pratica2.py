# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

#Solicitando ao usuário um valor
n = input('Digite um valor:')

# Qual o tipo (Boleano, Float, Inteiro, String)
print("Qual o seu tipo?", type(n))

# O "is...." verifica se o valor digitado é algo
print("É uma letra?", n.isalpha())
print("É um número?", n.isnumeric())
print("É um alfanumerico?", n.isalnum())
print("Está em maiúsculo?", n.isupper())
