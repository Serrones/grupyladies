# exercicio dictionary


dog = {'raça':'schnauzer','idade':'03 anos','cor':'Sal e Pimenta'}

print(dog['raça'])
print(dog['idade'])
print(dog['cor'])

dog['cor'] = 'Preto e Prata'

print('Alterada a cor:', dog['cor'])

dog['sexo']='fêmea'

print('Acrescentado novo atributo:', dog['sexo'])

print(dog)

del dog['sexo']

print(dog)

print(dog.get('tamanho', 'Chave inexistente'))
