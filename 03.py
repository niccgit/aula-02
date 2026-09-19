# Escreva um programa em Python que receba as seguintes informações do usuário:
#
# Renda Mensal (float)
# Score (int number between 0 and 1000)
# Possui Bens como garantia? (S or N)
# Tem Histórico de Inadimplência? (S or N)
#
# Para ser aprovado precisa encaixar ou na REGRA 1 OU na REGRA 2. Logo:
#
# REGRA 1
#
# Ter Renda Mensal >= R$3.000,00
# Ter Score >= 600
# Não ter Histórico de Inadimplência
#
# REGRA 2
#
# Independentemente da Renda Mensal OU do Score é preciso:
# Não ter Histórico de Inadimplência
# Possuir Bens de garantia
#
# Se o cliente encaixar na REGRA 1 ou na REGRA 2, ele será aprovado.
# Se o cliente não se encaixar em nenhuma das regras, ele será reprovado.


opcoes_bens = ["sim", "não", "nao"]

opcoes_historico = ["sim", "não", "nao"]


renda_mensal = float(input("Digite a sua renda mensal: "))

score = int(input("Digite o seu score, entre 0 e 1000: "))

bens_de_garantia = input("Você possui bens de garantia? Responda com 'Sim' ou 'Não'").lower()

while bens_de_garantia not in opcoes_bens:
    bens_de_garantia = input("Resposta inválida! Responda somente com 'Sim' ou 'Não'").lower()

historico_inadimplencia = input("Você possui histórico de inadimplência? Responda com 'Sim' ou 'Não'").lower()

while historico_inadimplencia not in opcoes_historico:
    historico_inadimplencia = input("Resposta inválida! Responda somente com 'Sim' ou 'Não'").lower()


if renda_mensal >= 3000 and score >= 600 and (historico_inadimplencia == "não" or historico_inadimplencia == "nao"):
    print("Seu empréstimo está aprovado!")
elif (historico_inadimplencia == "não" or historico_inadimplencia == "nao") and bens_de_garantia == "sim": 
    print("Seu empréstimo está aprovado!")
else:
    print("Seu empréstimo não foi aprovado...")
