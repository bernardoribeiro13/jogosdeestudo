import random


def jogo_forca():

  print("╔═══════════════╗")
  print("     olaaa!")
  print("╚═══════════════╝")
  
  
  #project == forca
  
  print("»»————-　★　————-««")
  print("bem-vindo ao jogo de forca")
  print("»»————-　★　————-««")

  print("adivinhe a palavra!")
  
  palavras = []
  
  palavras_aleatorias = open("br-sem-acentos.txt", "r")

  
  while True:
    print("niveis: facil, medio, dificil")
    nivel_escolhido = input("qual nivel voce quer jogar? ")
    
    if nivel_escolhido == "facil":
      for linhas in palavras_aleatorias:
        if len(linhas) < 5:
          linhas = linhas.strip()
          palavras.append(linhas)
      break
    elif nivel_escolhido == "medio":
      for linhas in palavras_aleatorias:
        if len(linhas) >= 5 and len(linhas) < 10:
          linhas = linhas.strip()
          palavras.append(linhas)
      break
    elif nivel_escolhido == "dificil":
      for linhas in palavras_aleatorias:
        if len(linhas) >= 1 and len(linhas) < 15:
          linhas = linhas.strip()
          palavras.append(linhas)
      break
    else:
      printint("sinto muito que nivel que jogar? ")
      continue    
      
  index_lista_palavra = random.randrange(0, len(palavras))

  palavras_aleatorias.close()

  palavra_secreta = palavras[index_lista_palavra].lower()

  #print(palavra_secreta)
  
  letras_secretas = []
  
  enforcou = 6
    
  for letra in palavra_secreta:
    letras_secretas.append("_")  
    
  print(letras_secretas)
  
  while enforcou >= 1 or acertou == False:
    
    acertou = "_" not in letras_secretas
    chute_jogador = input("Qual letra? ")
    chute_jogador = chute_jogador.strip()

    index = 0
    
    if chute_jogador in palavra_secreta:
      for letra in palavra_secreta:
        if (chute_jogador.upper() == letra.upper()):
          letras_secretas[index] = letra
        index = index + 1
      
      print(letras_secretas)
    
    else:
      print("try again!")
      enforcou -=1
  
    if acertou == True:
      print("parabens! voce acertou. a palavra era {}".format(palavra_secreta))
      break
  
    elif enforcou <= 0:
      print("ENFORCADO")
      print("a palavra era: {}".format(palavra_secreta))
            
      break
  
  print("fim de jogo")
    
if(__name__ == '__main__'):
    jogar()