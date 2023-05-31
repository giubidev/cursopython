# Faça um sorteio de alunos 

# Importando a biblioteca
import random

# Solicitando ao usuário os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: )")

# Criando listas
lista = [aluno1, aluno2, aluno3, aluno4]

# Sorteando o aluno escolhido
escolhido = random.choice(lista)

# Exibindo o aluno escolhido
print("O aluno escolhido foi {}".format(escolhido))
