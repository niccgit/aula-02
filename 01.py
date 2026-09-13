# Escreva um programa em Python que peça as seguintes três informações do usuário:
#
# Idade do visitante (int)
# Altura do visitante (int) - em centímetros 
# Autorização dos pais (str) - S ou N
#
# O programa deve exibir "Acesso liberado!", se o visitante atender às regras de uso dos brinquedos
#
# CASO CONTRÁRIO 
#
# O programa deve exibir "Acesso negado.", se o visitante não atender às regras de uso dos brinquedos
#
# AS REGRAS SÃO:
#
# Ter idade maior ou igual à 12 anos de idade E Ter altura maior ou igual à 140 centímetros 
# !!!! OU !!!!
# Ter a Autorização dos pais


idade_visitante = int(input("Qual é a sua idade?"))
altura_visitante = int(input("Qual é a sua altura (em centímetros)?"))
autorizacao = input("Você tem a autorização dos seus pais? Responda com 'Sim' ou 'Não'").lower()

opcoes_autorizacao = ["sim", "não", "nao"]


while autorizacao not in opcoes_autorizacao:
    autorizacao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não'").lower()


if idade_visitante >= 12 and altura_visitante >= 140 or autorizacao == "sim": 
    print("Acesso liberado!")
else:
    print("Acesso negado.")
