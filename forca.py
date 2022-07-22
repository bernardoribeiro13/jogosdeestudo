import random


def jogo_forca():

   
  print("╔═══════════════╗")
  print("     olaaa!")
  print("╚═══════════════╝")
  print("\n")
      
  
    
  print("»»————-　★　————-««")
  print("bem-vindo ao jogo de forca")
  print("»»————-　★　————-««")
  print("\n")
    
  print("adivinhe a palavra!")

  palavras = []
  
  
  #possibilidades de palavras extraidas do arquivo anexo
    
  palavras_aleatorias = open("br-sem-acentos.txt", "r")
  
  
  #sistema de seleção de niveis baseado na quantidades de letras da palavra secreta


  while True:
    print("niveis: facil, medio, dificil")
    print("\n")
    nivel_escolhido = input("qual nivel voce quer jogar? ")
    print("\n")
        
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
      print("\n")
      continue    


#sistema de escolha aleatoria de palavra a ser adivinhada
  index_lista_palavra = random.randrange(0, len(palavras))
    
  palavras_aleatorias.close()
    
  palavra_secreta = palavras[index_lista_palavra].lower()

#função print para teste de palavra
  
  #print(palavra_secreta)
  
  letras_secretas = []
  
  enforcou = 6

  if enforcou == 6:
       print("esse é o jão")
       print("\n")
       print("(.❛ᴗ❛.)")
       print(" /||\   ")
       print("  /\\")
       print("\n")
       print("salve o jão")
       print("\n")
      
  for letra in palavra_secreta:
    letras_secretas.append("_")  
    
  print(letras_secretas)

#loop do jogo
  while enforcou >= 1 or acertou == False:
               
    acertou = "_" not in letras_secretas
    
    chute_jogador = input("Qual letra? ")
    print("\n")
    chute_jogador = chute_jogador.strip()

    index = 0
    
    if chute_jogador in palavra_secreta:
      for letra in palavra_secreta:
        if (chute_jogador.upper() == letra.upper()):
          letras_secretas[index] = letra
        index = index + 1
      
      print(letras_secretas)
    
    else:
      print("tente de novo!")
      print("\n")
      enforcou -=1
      if enforcou == 5:
        print("oops, pobre jão")
        print("\n")
        print("____")
        print("[  |")
        print("[  | ")
        print("[ (❛ᴗ❛) ")
        print("[")
        print("\n")
      elif enforcou == 4:
        print("jão esta correndo perigo")
        print("\n")
        print("____")
        print("[  |")
        print("[  | ")
        print("[ (❛ᴗ❛) ")
        print("[  ||   ")
        print("\n")
      elif enforcou == 3:
        print("jão esta começando a ficar nervoso")
        print("\n")
        print("____")
        print("[  |")
        print("[  | ")
        print("[(・_・)")
        print("[ /||   ")
        print("\n")
      elif enforcou == 2:
        print("jão esta com muito medo")
        print("\n")
        print("____")
        print("[  |")
        print("[  | ")
        print("[ (;_;)")
        print("[ /||\   ")
        print("\n")
      elif enforcou == 1:
        print("jão esta começando a ficar desesperado")
        print("\n")
        print("________")
        print("[       |")
        print("[       | ")
        print("[ 。゜(´Ｏ`) ゜゜。")
        print("[      /||\   ")
        print("[        / ")
        print("\n")
      
    if acertou == True:
      print("parabens! voce acertou. a palavra era {}".format(palavra_secreta))
      print("jão muito agradecido")
      print("olha jão dansçando")
      print("\n")
      print("(￣▽￣)")
      print(" 〜//〜")
      print("  '\\'")
      print("\n")
      print("(￣▽￣)")
      print(" 〜\\\〜")
      print("  '//'")
      break
  
    elif enforcou <= 0:
      print("ENFORCADO")
      print("a palavra era: {}".format(palavra_secreta))
      print("\n")
      print("pobre jãp")
      print("\n")
      print("(x.x)")
      print(" /||\   ")
      print("  /\\")
      print("\n")
      print("dascense em paz jão")
      print("\n")
      print("\n")
      print("jão não sera esquecido")
      print("\n")
      print("( ´-ω･)︻┻┳══━一")   
      print("\n")

      
            
      break

  print("fim de jogo")

if(__name__ == '__main__'):
  jogar()