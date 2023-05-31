# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

# Solicitando preço para o usuário
preco = float(input("Digite o preço atual do produto: "))

# Valor do desconto
desc = preco * 0.005

# Novo valor com o desconto
novo = preco * 0.95

# Exibindo na tela o novo valor com desconto 
print("Valor inicial: {}".format(preco))
print("Valor do desconto: {}".format(desc))
print("Valor a pagar: {}".format(novo))

