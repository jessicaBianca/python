#Condicional
saldo = 200

if(saldo >= 200):
    saldo += 100
    print("Saldo atual: ", saldo)
elif(saldo < 200):
    print("Não ganha nada! ")



#if aninhado
conta_universitario = False
conta_normal = True
saldo = 999

if conta_universitario:
    if(saldo < 1000):
        print("Pouco saldo!")
    elif(saldo >=1000):
        print("Bom saldo !")
elif(conta_normal):
    print("Conta normal, Tudo OK")



#if ternário
resultado = "Sucesso, saldo maior ou igual a 1K" if saldo>=1000 else "Falhou, saldo abaixo de 1K"
print(resultado)

#Repetição - Usada para repetir trecho de código um determinado numero de vezes

for i in range(1, 6):  # O range vai de 1 a 5
    print(i)


contador = 0
while contador < 3:  # Enquanto contador for menor que 3
    print("Olá")
    contador += 1  # Incrementa o contador
