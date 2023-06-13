# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"

cidade = input("Digita o nome de uma cidade: ")

cidadegg = cidade.upper()
vv = cidadegg.find("SANTO", 0, 5)

if vv == -1:
    print('A cidade não começa com a palavra "SANTO"')

else:
    print('A cidade começa com a palavra "SANTO"')
