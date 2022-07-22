import adivinhação
import forca

#menu de escolha de jogo
#boas vindas para o usuario


def escolha_jogo():

    print("╔═══════════════╗")
    print("     olaaa!")
    print("╚═══════════════╝")
    print("\n")

    #disponibilidade de possibilidades de jogos
    print("»»————-　★　————-««")
    print("escolha seu jogo")
    print("»»————-　★　————-««")
    print("\n")

    print("forca ou adivinhaçao?")

    #while loop para os resultados das escolhas

    while True:
        jogo = input("qual jogo para hoje? ")
        if jogo == "forca":
            print("voce escolheu forca")
            forca.jogo_forca()
            print("\n")
            break
        elif jogo == "adivinhaçao":
            print("voces escolheu adivinhação")
            print("\n")
            adivinhação.jogo_adivinhaçao()
            break
        else:
            print("erro. não entendi muito bem, pode repetir?")
            continue


if (__name__ == "__main__"):
    escolha_jogo()
