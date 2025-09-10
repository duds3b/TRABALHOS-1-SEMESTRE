import random
querer = True
papel = 1
pedra = 2
tesoura = 3
tela = 0
choice = 1
nome_move1 = ""
nome_move2 = ""

while querer == True:
    tela = int(input("bem vindo ao jokempo digite o modo que voce quer jogar: (pessoa x pessoa = 1) (pessoa x computador = 2) (computador x computador = 3)"))

    ##CASO O JOGADOR SELECIONE A PRIMEIRA TELA QUE É PESSOA CONTRA PESSOA
    if tela == 1:
        p1 = int(input("Digite a primeira jogada: (1 para papel) (2 para pedra) e (3 para tesoura)"))
        p2 = int(input("Digite a segunda jogada: (1 para papel) (2 para pedra) e (3 para tesoura)"))


         ##ATRELANDO O NUMERO COM O NOME P1 E P2
        if p1 == 1:
            nome_move1 = "papel"
        elif p1 == 2:
            nome_move1 = "pedra"
        elif p1 == 3:
            nome_move1 = "tesoura"

        if p2 == 1:
            nome_move2 = "papel"
        elif p2 == 2:
            nome_move2 = "pedra"
        elif p2 == 3:
            nome_move2 = "tesoura"


        ##CASO SEJA EMPATE
        if p1 == p2:
            print(f"Empate! Ambos jogaram {nome_move1}")

        ##CASO SEJA PAPEL
        if p1 == 1 and p2 == 2:
            print(f"Você venceu! p1 jogou {nome_move1} e p2 jogou {nome_move2}")
        elif p1 == 1 and p2 == 3:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e p2 jogou {nome_move2}")

        ##CASO SEJA PEDRA
        if p1 == 2 and p2 == 3:
            print(f"Você venceu! p1 jogou {nome_move1} e p2 jogou {nome_move2}")
        elif p1 == 2 and p2 == 1:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e p2 jogou {nome_move2}")

        ##CASO SEJA TESOURA
        if p1 == 3 and p2 == 1:
            print(f"Você venceu! p1 jogou {nome_move1} e p2 jogou {nome_move2}")
        elif p1 == 3 and p2 == 2:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e p2 jogou {nome_move2}")

        choice = input("Você quer continuar? y ou n: ")
        if choice == "n":
            tela = 0
            querer = False

    ##CASO O JOGADOR ESCOLHA A SEGUNDA TELA, PESSOA X BOT
    if tela == 2:
        p1 = int(input("Digite a primeira jogada: (1 para papel) (2 para pedra) e (3 para tesoura): "))
        p2 = random.randint(1, 3)

         ##ATRELANDO O NUMERO COM O NOME P1 E P2
        if p1 == 1:
            nome_move1 = "papel"
        elif p1 == 2:
            nome_move1 = "pedra"
        elif p1 == 3:
            nome_move1 = "tesoura"

        if p2 == 1:
            nome_move2 = "papel"
        elif p2 == 2:
            nome_move2 = "pedra"
        elif p2 == 3:
            nome_move2 = "tesoura"


        ## CASO SEJA EMPATE
        if p1 == p2:
            print(f"Empate! Ambos jogaram {nome_move1}")

        ## CASO SEJA PAPEL
        if p1 == 1 and p2 == 2:
            print(f"Você venceu! p1 jogou {nome_move1} e bot jogou {nome_move2}")
        elif p1 == 1 and p2 == 3:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e bot jogou {nome_move2}")

        ## CASO SEJA PEDRA
        if p1 == 2 and p2 == 3:
            print(f"Você venceu! p1 jogou {nome_move1} e bot jogou {nome_move2}")
        elif p1 == 2 and p2 == 1:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e bot jogou {nome_move2}")

        ## CASO SEJA TESOURA
        if p1 == 3 and p2 == 1:
            print(f"Você venceu! p1 jogou {nome_move1} e bot jogou {nome_move2}")
        elif p1 == 3 and p2 == 2:
            print(f"Você perdeu, poxa! p1 jogou {nome_move1} e bot jogou {nome_move2}")

        choice = input("Você quer continuar? (y ou n): ")
        if choice == "n":
            tela = 0
            querer = False

    ##CASO O JOGADOR ESCOLHA BOT X BOT
    if tela == 3:
        p1 = random.randint(1, 3)
        p2 = random.randint(1, 3)

         ##ATRELANDO O NUMERO COM O NOME P1 E P2
        if p1 == 1:
            nome_move1 = "papel"
        elif p1 == 2:
            nome_move1 = "pedra"
        elif p1 == 3:
            nome_move1 = "tesoura"

        if p2 == 1:
            nome_move2 = "papel"
        elif p2 == 2:
            nome_move2 = "pedra"
        elif p2 == 3:
            nome_move2 = "tesoura"


        ## CASO SEJA EMPATE
        if p1 == p2:
            print(f"Empate! Ambos jogaram {nome_move1}")

        ## CASO SEJA PAPEL
        if p1 == 1 and p2 == 2:
            print(f"O BOT 1 VENCEU! p1 jogou {nome_move1} e p2 jogou {nome_move2}")
        elif p1 == 1 and p2 == 3:
            print(f"O BOT 2 VENCEU BOT 1 jogou {nome_move1} e BOT 2 jogou {nome_move2}")

        ## CASO SEJA PEDRA
        if p1 == 2 and p2 == 3:
            print(f"O BOT 1 VENCEU! O BOT 1 JOGOU {nome_move1} e BOT 2 jogou {nome_move2}")
        elif p1 == 2 and p2 == 1:
            print(f"O BOT 2 VENCEU O BOT 1 JOGOU {nome_move1} e BOT 2 jogou {nome_move2}")

        ## CASO SEJA TESOURA
        if p1 == 3 and p2 == 1:
            print(f"O BOT 1 VENCEU! O BOT 1 JOGOU {nome_move1} e BOT 2 jogou {nome_move2}")
        elif p1 == 3 and p2 == 2:
            print(f"O BOT 2 VENCEU! O BOT 1 JOGOU {nome_move1} e BOT 2 jogou {nome_move2}")

        choice = input("Você quer continuar? (y ou n): ")
        if choice == "n":
            tela = 0
            querer = False
