#Ex 3

x = 1
soma = 0

while x <= 5:
    gasto = float(input('Quanto você gastou hoje?\n'))
    soma = soma + gasto
    x = x + 1

print('Gasto semanal:',soma)
