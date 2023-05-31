# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

# Solicitando o valor do salario
salario = float(input("Digite o valor do seu salário: "))

# Calculo do valor do aumento
aumento = salario * 0.15

# Soma do salário com o valor do aumento
novo = salario + aumento

# Exibindo na tela os valores
print("Salário atual: {}".format(salario))
print("Valor do aumento: {}".format(aumento))
print("Novo salário: {}".format(novo))
