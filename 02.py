# Escreva um programa em python que pergunte tres informações do usuario
# Você é estudante?
# Qual é o dia da semana? (Terça-feira ou outro dia?)
# Qual é o tipo da sala? (VIP ou Comum?)
# 
# O programa deve exibir "Desconto aplicado!" se for um Estudante ou um cara numa terça-feira na sala comum

estudante = input("Você é estudante? Responda com 'Sim'ou 'Não'")
dia_da_semana = input("Hoje é Terça-feira? Responda com 'Sim'ou 'Não'")
tipo_da_sala = input("Qual o tipo da sala? VIP ou Comum?")

desconto_aplicado = estudante == "Sim" and tipo_da_sala == "Comum"
desconto_aplicado = dia_da_semana == "Sim" and tipo_da_sala == "Comum"

valor_integral = estudante == "Não" and tipo_da_sala == "VIP"

if estudante == "Sim" and tipo_da_sala == "Comum":
    print(desconto_aplicado)
elif dia_da_semana == "Sim" and tipo_da_sala == "Comum":
    print(desconto_aplicado)
else:
    print(valor_integral)