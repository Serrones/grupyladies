# exercicio 01 - pyladies - função while

contador = 1
soma = 0

while contador <= 3:
    nums = int(input('Favor digitar um número:'))
    soma = soma + nums
    contador += 1
    if contador <= 3:
        print('soma parcial:',soma)
        print('incrementador:',contador)
print('Soma total:',soma)
