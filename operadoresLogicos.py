# and (ambos devem ser atendidos) ou or (ou um ou outro deve atender)

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <=limite)

print((saldo >= saque) and (saque <=limite))

print(saldo >= saque or saque <=limite)


print("Resultado: ", (saldo == 100 and saque == 200) and (saldo > 900 and limite <200))


#operador de negação: not
#Exemplo:
print(not saldo < saque)