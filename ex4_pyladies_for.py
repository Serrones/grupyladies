# exercicio For


lista = range(1,11)
soma = 0
# lista = [1,2,3,4,5,6,7,8,9,10]
impar = []

print(lista)

for i in lista:
    if i % 2 != 0:
        soma = soma + i
        impar.append(i)

print(impar)
print('Soma total dos números ímpares:', soma)
