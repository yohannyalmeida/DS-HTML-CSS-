import random
def jogo_adivinhacao():
    numero_secreto=random.randint(1,10)
    tentativas= 0
    max_tentativas=5

    print("bem-vindo ao jogo de adivinhação")
    print("tente adivinha o número entre 1 e 100.")

    while tentativas < max_tentativas:
        tentativa=int(input("digite o seu palpite"))

        if  tentativa < numero_secreto:
         print("O número secreto é maior.") 

        elif tentativa > numero_secreto:
         print("O número secreto é menor.")
        else:
         print(f"parabéns vocé acertou o número secreto,que era.{numero_secreto}")         
         break
        tentativas +=1
        print(f"vocé tem {max_tentativas-tentativas} tentativas restantes.")
    else: 
      print(f"voce excedeu o número máximo de tentativas. o número secreto era{numero_secreto}.")

jogo_adivinhacao()



