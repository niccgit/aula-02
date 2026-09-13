# Escreva um programa em Python que pergunte as seguintes três informações do usuário:
#
# Você é estudante?
# Qual é o dia da semana? (Terça-feira ou outro dia?)
# Qual é o tipo da sala? (VIP ou Comum?)
#
# O programa deve exibir "Desconto aplicado!" se for um Estudante + Sala Comum
# OU
# O programa deve exibir "Desconto aplicado!" se for uma Terça-feira + Sala Comum
# CASO CONTRÁRIO 
# O programa deve exibir "Valor integral."


opcoes_estudante = ["sim", "não", "nao"]
opcoes_dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
opcoes_sala = ["vip", "comum"]


estudante = input("Você é estudante? Responda com 'Sim' ou 'Não': ").lower()

while estudante not in opcoes_estudante:
    estudante = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()


dia_da_semana = input("Hoje é que dia da semana?").lower()

while dia_da_semana not in opcoes_dias:
    dia_da_semana = input("Resposta inválida! Responda apenas com o dia da semana: ").lower()


tipo_da_sala = input("Qual o tipo da sala? VIP ou Comum? ").lower()

while tipo_da_sala not in opcoes_sala:
    tipo_da_sala = input("Resposta inválida! Responda somente com 'VIP' ou 'Comum': ").lower()


if (estudante == "sim" and tipo_da_sala == "comum") or (dia_da_semana == "terça-feira" and tipo_da_sala == "comum"):
    print("Desconto aplicado!")
else:
    print("Valor integral.")
