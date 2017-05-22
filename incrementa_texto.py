def leitura():
    with open('zen.txt','r') as f:
        conteudo = f.read()
        print(conteudo)
    return conteudo

with open('zen2.txt','a') as f:
    f.write(leitura())
