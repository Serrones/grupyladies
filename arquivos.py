def escreve_novo_zen():
    word = input('Favor entrar com uma palavra:\n')
    with open('zen.txt','r') as leitura:
        for linha in leitura:
            if word in linha:
                with open('zen2.txt','a') as gravador:
                    gravador.write(linha)

escreve_novo_zen()

with open('zen2.txt','r') as f:
    conteudo = f.read()
    print(conteudo)
