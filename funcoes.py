import os


def limparTela():
    os.system("cls")


def jogadores(desafiante, competidor):
    nomesParticipantes = []
    nomesParticipantes.append(desafiante)
    nomesParticipantes.append(competidor)
    return nomesParticipantes


def dicas(dica1, dica2, dica3):
    dicas = []
    dicas.append(dica1)
    dicas.append(dica2)
    dicas.append(dica3)
    return dicas


def relatorio(desafiante, competidor, palavraChave, vencedor):
    arquivo = open("relatorio.txt", "a")
    if vencedor == competidor:
        arquivo.write(
            f"Vencedor: {competidor}, Perdedor: {desafiante}, Palavra Chave: {palavraChave}\n")
        arquivo.write("\n")
    else:
        arquivo.write(
            f"Vencedor: {desafiante}, Perdedor: {competidor}, Palavra Chave: {palavraChave}\n")
        arquivo.write("\n")
    arquivo.close


def verRelatorio():
    arquivo = open("relatorio.txt", "r")
    texto = arquivo.readlines()
    arquivo.close()
    return texto


def mensagemVencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("")


def mensagemPerdedor():
    print("        \         /      ")
    print("         \       /  ")
    print("          \     /    ")
    print("           \   /       ")
    print("            \ /      ")
    print("            / \      ")
    print("           /   \         ")
    print("          /     \        ")
    print("         /       \       ")
    print("        /         \      ")
    print("")
