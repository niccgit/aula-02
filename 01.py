# Escreva um programa em pythonque peça as seguintes informacoes:
# idade (numero inteiro)
# altura em centimetros ( numero inteiro)
# autorizacao dos pais (sim ou nao)
#
# o programa deve exibir "acesso liberado", se o visitante puder andar no brinquedo
# o programa devev exibir "acesso negado", caso contrario
#
# AS REGRAS SAO:
# ter idade >= 12 anos de idade
# !!!! E !!!!!
# ter altura >= 140 de altura
# !!!! OU !!!!
# se tiver a autorizacao dos pais

idade = int(input ("Olá! Digite a sua idade: "))
altura = int(input ("Agora digite a sua altura (em centímetros): "))
autorizacao_dos_pais = input("Você tem a autorização dos seus pais?")

autorizacao_dos_pais = "sim"

if idade >= 12 and altura >= 140 or autorizacao_dos_pais == "sim":
    print("Acesso liberado!")
else:
    print("Acesso negado.")