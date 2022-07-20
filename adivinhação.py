def jogo_adivinhaçao():
  
  print("╔═══════════════╗")
  print("     olaaa!")
  print("╚═══════════════╝")
  
  #project == number game
  
  import random
  
  print("»»————-　★　————-««")
  print("bem-vindo ao jogo de adivinhação")
  print("»»————-　★　————-««")
  
  numero_secreto = random.randrange(1, 101)
  #print(numero_secreto)
  #acima para teste sobre o numero a adivinhar
  #pontuação inicial a ser subtraida com o passar de jogo
  
  pontuação = 0
  
  print("facil, medio ou dificil")
  #loop de seleção de nivel
  
  while True:
    nivel_dificuldade = input("qual nivel voce deseja? ")
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
      continue
  #numero de rodadas inicial:
  numero_rodadas = 1
  
  #loop while para o jogo em si com a pontuação como limitante
  
  print("sua pontuação inicial é: " + str(pontuação))
  
  while int(tentativas_disponiveis) >= numero_rodadas or pontuação >= 0:
    
    print("Rodada {} de {}". format(numero_rodadas, tentativas_disponiveis))
      
    chute = input("digite seu numero(entre 1 e 100): ")
    chute_int = int(chute)
      
    
    if 1 > chute_int or chute_int > 100:
       print("erro! entre 1 e 100, por favor!")
       continue
    elif numero_secreto == chute_int:
       print("parabens!!")
       print("sua pontuação é: " + str(pontuação))
       break
    else:
  #dica para o usuario se o numero que foi chutado é maior ou menor que
      
      if numero_secreto < chute_int:
        print("sinto muito, numero muito alto")
        pontuação -= 10
        print("sua pontuação agora é: " + str(pontuação))
      elif numero_secreto > chute_int:
        print("sinto muito, numero muito baixo")
        pontuação -= 10
        print("sua pontuação agora é: " + str(pontuação))
      
    numero_rodadas += 1
  
  print("fim de jogo")