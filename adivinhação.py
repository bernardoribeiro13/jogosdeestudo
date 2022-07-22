#boas vindas ao jogo de adivinhação
import random
  

def jogo_adivinhaçao():

  
  print("╔═══════════════╗")
  print("     olaaa!")
  print("╚═══════════════╝")
  print("\n")
    
  
  
  print("»»————-　★　————-««")
  print("bem-vindo ao jogo de adivinhação")
  print("»»————-　★　————-««")
  print("\n")

#escolha do numero a ser adivinhado com a biblioteca random
  numero_secreto = random.randrange(1, 101)

#print(numero_secreto)
#acima para teste sobre o numero a adivinhar
#pontuação inicial a ser subtraida com o passar de jogo

  pontuação = 0
  
  print("facil, medio ou dificil")
  print("\n")
  #loop de seleção de nivel
  
  while True:
    nivel_dificuldade = input("qual nivel voce deseja? ")
    print("\n")
    if nivel_dificuldade == "facil":
      tentativas_disponiveis = 20
      pontuação += 200
      break
    elif nivel_dificuldade == "medio":
      tentativas_disponiveis = 10
      pontuação += 100
      break
    elif nivel_dificuldade == "dificil":
      tentativas_disponiveis = 5
      pontuação += 50
      break
    else:
      print("não entendi, tente de novo")
      print("\n")
      continue
  #numero de rodadas inicial:
  numero_rodadas = 1
  
  #loop while para o jogo em si com a pontuação como limitante
  
  print("sua pontuação inicial é: " + str(pontuação))
  print("\n")


  while int(tentativas_disponiveis) >= numero_rodadas or pontuação >= 0:
    
    print("Rodada {} de {}". format(numero_rodadas, tentativas_disponiveis))
    print("\n")
      
    chute = input("digite seu numero(entre 1 e 100): ")
    chute_int = int(chute)
    print("\n")
      
    
    if 1 > chute_int or chute_int > 100:
       print("erro! entre 1 e 100, por favor!")
       print("\n")
       continue
    elif numero_secreto == chute_int:
       print("parabens!!")
       print("\n")
       print("sua pontuação é: " + str(pontuação))
       print("\n")
       break
    else:
  #dica para o usuario se o numero que foi chutado é maior ou menor que
      
      if numero_secreto < chute_int:
        print("sinto muito, numero muito alto")
        print("\n")
        pontuação -= 10
        print("sua pontuação agora é: " + str(pontuação))
        print("\n")
      elif numero_secreto > chute_int:
        print("sinto muito, numero muito baixo")
        print("\n")
        pontuação -= 10
        print("sua pontuação agora é: " + str(pontuação))
        print("\n")
      
    numero_rodadas += 1

print("fim de jogo")