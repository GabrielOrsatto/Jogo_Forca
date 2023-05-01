import funcoes

funcoes.limparTela()

print("BEM VINDO AO JOGO DA FORCA\n")

print("Alunos: Gabriel Pradegan Orsatto e Pedro Luan Rodrigues\n")

while True:
    desafiante = input("Digite o nome do desafiante: ")
    competidor = input("Digite o nome do competidor: ")
    funcoes.jogadores(desafiante, competidor)

    palavra = input("Digite a palavra: ")
    respostasDicas = ["1ª Dica: ", "2ª Dica: ", "3ª Dica: "]
    listaDicas = []

    for i in range(len(respostasDicas)):
        print(respostasDicas[i])
        listaDicas.append(input())

    funcoes.limparTela()

    print("A palavra é composta por", len(palavra), "letras.")
    for i in range(len(palavra)):
        print(end="")

    erros = 0
    tentativas = []
    acertos = []
    vencedor = []

    while True:
        print("\n")
        print("Regras do jogo: (1) para jogar - (2) para dicas")
        print("(1) Jogar")
        print("(2)Dicas", len(ListaDicas), "restantes")
        print("Erro: ", erros)

        escolha = input()
        if escolha == "1":
            funcoes.limparTela()

            letra = input("Digite uma letra: ")
            if letra in tentativas:
                print("Você já digitou essa letra")
            elif letra not in palavra:
                print("A palavra não possui a letra: ", Letra)
                tentativas.append(letra)
                erros += 1
            else:
                print("Você acertou")
                acertos.append(letra)
                resposta = ""
                for letra in palavra:
                    if letra in acertos:
                        resposta += letra
                    else:
                        palavra += "*"
                print(resposta)
                if resposta == palavra:
                    print("Parabéns! Você acertou!")
                    vencedor = competidor
                    break
        elif escolha == "2":
            funcoes.limparTela()

            try:
                print(listaDicas[0])
                del listaDicas[0]
            except:
                print("Suas dicas acabaram!")
        else:
            print("Opção inválida!")

        if erros >= 5:
            print("Que pena! Você perdeu!")
            break

    funcoes.relatorio(desafiante, competidor, palavra, vencedor)
    texto = funcoes.verRelatorio()
    for i in texto:
        texto = i.strip('\n')
        print(texto)

    print("\n(1) Sair.")
    print("(2) Jogar novamente.")
    escolha2 = input()
    if escolha2 == "1":
        break
    elif escolha2 == "2":
        pass
    else:
        print("Opção inválida!")
