# %, +, format , f string (+usada)

nome = "Jessica"
idade = 18
profissao = "Engenheira"
linguagem = "python"

#old string
print("Eu sou a %s" % (nome))

#format
print("Olá, me chamo {}.".format(nome))
print("Olá, me chamo {0}.".format(nome))

#f string
print(f"Olá, me chamo {nome}")

#f string para formatar número 
PI = 3.14159
print(f"PI: {PI:.2f}")