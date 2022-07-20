import adivinhação
import forca

def escolha_jogo():
    
  
  print("╔═══════════════╗")
  print("     olaaa!")
  print("╚═══════════════╝")
  
  print("»»————-　★　————-««")
  print("escolha seu jogo")
  print("»»————-　★　————-««")
  
  
  print("forca ou adivinhaçao?")

  while True:
    jogo = input("qual jogo para hoje? ")
    if jogo == "forca":
      print("voce escolheu forca")
      forca.jogo_forca()
      break
    elif jogo == "adivinhaçao":
      print("voces escolheu adivinhação")
      adivinhação.jogo_adivinhaçao()
      break
    else:
      print("erro. não entendi muito bem, pode repetir?")
      continue
  
if (__name__ == "__main__"):
  escolha_jogo()