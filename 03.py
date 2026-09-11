# Escreva um programa em python que receba as seguintes informações  do usuario:
# Renda Mensal (float number)
# Score (int number between 0 and 1000)
# Possui Bens como garantia? (Y or N)
# Tem Histórico de Inadimplência? (Y or N)
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
# Se o cliente encaixar na REGRA 1 OU na REGRA 2, ele será aprovado.
# Se o cliente não encaixar em NENHUMA das regras, ele será reprovadp.

renda_mensal = float(input("Digite a sua renda mensal: "))
score = int(input("Digite o seu score, entre 0 e 1000: "))
bens_de_garantia = input("Você possui bens de garantia?")
historico_inadimplência = input("Você possui histórico de inadimplência?")

opcoes3 = ['sim', 'não', 'nao']
opcoes4 = ['sim', 'não', 'nao']

if renda_mensal >= 3000 and score >= 600 and historico_inadimplência == 'não' or 'nao':
    print("Seu empréstimo está aprovado!")
elif historico_inadimplência == 'não' or 'nao' and bens_de_garantia == 'sim':
    print("Seu empréstimo está aprovado!")
else:
    print("Seu empréstimo não foi aprovado...")