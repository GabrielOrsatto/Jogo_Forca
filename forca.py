import funcoes

funcoes.limparTela()

print("JOGO DA FORCA\n")

while True:
    desafiante = input("Desafiante: ")
    competidor = input("Competidor: ")
    funcoes.jogadores(desafiante, competidor)

    palavraChave = input("\nDigite a palavra chave: ").upper()
    respostasDicas = ["1ª Dica: ", "2ª Dica: ", "3ª Dica: "]
    dicas = []
    for i in range(len(respostasDicas)):
        print(respostasDicas[i])
        dicas.append(input())

    funcoes.limparTela()

    print("A palavra possui ", len(palavraChave), "letras.")
    for i in range(len(palavraChave)):
        print(end="")

    erros = 0
    tentativas = []
    acertos = []
    vencedor = []

    while True:
        print("\n")
        print("(1) Jogar")
        print("(2) Dicas (", len(dicas), "disponíveis).")
        print("Erro: ", erros)

        opcao = input()
        if opcao == "1":
            letra = input("\nDigite uma letra: ").upper()
            if letra in tentativas:
                print("Você já digitou essa letra.")
            elif letra not in palavraChave:
                print("A palavra não possui essa letra.")
                tentativas.append(letra)
                erros += 1
            else:
                print("Você acertou uma letra!")
                acertos.append(letra)
                palavra = ""
                for letra in palavraChave:
                    if letra in acertos:
                        palavra += letra
                    else:
                        palavra += "*"
                print(palavra)
                if palavra == palavraChave:
                    vencedor = competidor
                    funcoes.limparTela()
                    print("\nParabéns, você ganhou! A palavra era: ",
                          palavraChave, "\n")
                    funcoes.mensagemVencedor()
                    break
        elif opcao == "2":
            funcoes.limparTela()
            try:
                print("\nSua dica é: " + dicas[0])
                del dicas[0]
            except:
                print("\nSuas dicas acabaram!")
        else:
            print("Opção inválida!")

        if erros >= 5:
            print("Você perdeu!", "\n")
            funcoes.mensagemPerdedor()
            break

    funcoes.relatorio(desafiante, competidor, palavraChave, vencedor)
    texto = funcoes.verRelatorio()
    for i in texto:
        texto = i.strip('\n')
        print(texto)

    print("\n(1) Sair.")
    print("(2) Jogar novamente.")
    opcao2 = input()
    if opcao2 == "1":
        break
    elif opcao2 == "2":
        pass
    else:
        print("Opção inválida!")
