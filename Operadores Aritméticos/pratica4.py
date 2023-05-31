# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

# Solicitando o valor em metros para o usuário
metros = float(input("Digite o valor em metros: "))

# Convertando em centímetros e milímetros
cent = (metros * 100)
mil = (metros * 1000)

# Exibindo na tela o resultado da conversão
print("O valor em metros {}, é igual a {}cm e {}ml.".format(metros, cent, mil))


