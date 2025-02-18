#compara dois objetos e verifica se eles ocupam a mesma posição de memória

curso = "python"
nome_curso = curso
limite, saldo = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

#verifica se está na mesma posição de memória
print(limite is saldo)