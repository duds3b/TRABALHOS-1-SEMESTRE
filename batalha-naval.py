import random
from itertools import count
global countChoose
global cAleatorio
global lAleatorio



def sorteandoNumero():
    global cAleatorio, lAleatorio
    cAleatorio = random.randint(1, 10)
    lAleatorio = random.randint(1, 10)

def randomAdversario():
    for i in range(5):
      sorteandoNumero()
      while matrizAdversaria[cAleatorio-1][lAleatorio-1] != "O":
          sorteandoNumero()
      matrizAdversaria[cAleatorio-1][lAleatorio-1] = "X"


    pedindoUsuarioCasas()



def botEscolhendoCasa():
    sorteandoNumero()
    while matrizInterfaceBot[cAleatorio - 1][lAleatorio - 1] != "O":
        sorteandoNumero()
    matrizInterfaceBot[cAleatorio - 1][lAleatorio - 1] = "X"
    for linha in matrizInterfaceBot:
        print(linha)
    print(f"O bot escolheu as casas {cAleatorio} e {lAleatorio}")


def pedindoUsuarioCasas():
        while sum(l.count("X") for l in matrizJogador) < 5:
            vJogador = int(input("Digite uma casa de 1 a 10 na posicao vertical: "))
            while vJogador < 1 or vJogador > 10:
                print("ops! nao é valido")
                vJogador = int(input("Digite uma casa de 1 a 10 na posicao vertical: "))

            hJogador = int(input("Digite uma casa de 1 a 10 na posicao horizontal: "))
            while hJogador < 1 or hJogador > 10:
                print("ops! nao é valido")
                hJogador = int(input("Digite uma casa de 1 a 10 na posicao horizontal: "))


            while matrizJogador[vJogador - 1][hJogador - 1] != "O":
                print("Voce ja escolheu essa posicao, tente denovo")
                pedindoUsuarioCasas()

            if matrizJogador[vJogador - 1][hJogador - 1] == "O":
                matrizJogador[vJogador - 1][hJogador - 1] = "X"
                print(f"Voce escolheu sua {sum(l.count('X') for l in matrizJogador)} casa! sendo {vJogador} e {hJogador}")
        if sum(l.count("X") for l in matrizJogador) == 5:
            print("Aqui estão suas frotas abaixo:")
            for linha in matrizJogador:
                print(linha)

        jogo()


def jogo():
    naviosDerrubadosPlayer = 0
    naviosDerrubadosBot = 0

    print("OK! Vamos comecar, aqui esta seu tabuleiro de palpites pra ganhar do bot")
    while naviosDerrubadosPlayer < 5 and naviosDerrubadosBot < 5:
        for linha in matrizInterfacePlayer:
            print(linha)
        print(f"\nLEGENDA: X = Navio derrubado  O = Lugar que nao foi palpitado || Navios Que voce derrubou: {naviosDerrubadosBot}")
        palpiteV = int(input("\nDigite seu palpite na posicao vertical"))
        while palpiteV < 1 or palpiteV > 10:
            print("Opa! tem que ser de 1 a 10")
            palpiteV = int(input("\nDigite seu palpite na posicao vertical"))
        palpiteH = int(input("\nDigite seu palpite na posicao horizontal"))
        while palpiteH < 1 or palpiteH > 10:
            palpiteH = int(input("\nDigite seu palpite pra posicao horizontal"))
        matrizInterfacePlayer[palpiteV - 1][palpiteH - 1] = "X"
        if matrizAdversaria[palpiteV-1][palpiteH-1] == "X":
            matrizAdversaria[palpiteV-1][palpiteH-1] = "O"
            naviosDerrubadosBot += 1
            print("\nUMA FROTA FOI DESTRUIDA!!\n")
        else:
            print("Nenhuma frota encontrada nessa coordenada")
        print("Vez do bot!")
        botEscolhendoCasa()
        if matrizJogador[cAleatorio-1][lAleatorio-1] == "X":
            matrizInterfaceBot[cAleatorio-1][lAleatorio-1] = "X"
            print(f"UMA FROTA SUA FOI DESTRUIDA SE LASCOU!!! || Navios derrubados pelo bot: {naviosDerrubadosPlayer}")
            naviosDerrubadosPlayer +=1
        else:
            print(f"Nenhuma frota sua foi destruida pelo bot... ufa || Navios derrubados pelo bot: {naviosDerrubadosPlayer}")

    if naviosDerrubadosBot == 5:
        choice = int(input("Parabens!! Voce venceu, quer jogar o jogo de novo? 1 para SIM e 2 para NAO "))
    else:
        choice = int(input("Puts, voce perdeu, quer tentar outra vez? 1 para SIM e 2 para NAO "))

    while choice != 1 and choice != 2:
        choice = int(input("É 1 PARA SIM E 2 PARA NAO!!! DIGITE SUA RESPOSTA "))

    if choice == 1:
        resetandoMatrizes()
        randomAdversario()
    elif choice == 2:
        print("Entao ta bom falow")

matrizAdversaria =     [
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"]
]

matrizJogador =    [
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"]
]

matrizInterfacePlayer = [
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"]
]

matrizInterfaceBot =     [
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"],
    ["O","O","O","O","O","O","O","O","O","O"]
    ]

def resetandoMatrizes():

    global matrizAdversaria, matrizJogador, matrizInterfacePlayer, matrizInterfaceBot

    matrizAdversaria = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

    matrizJogador = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

    matrizInterfacePlayer = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

    matrizInterfaceBot = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]
randomAdversario()


