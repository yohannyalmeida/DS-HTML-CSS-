soma= 0
contador =0

print("digite os numeros para calcular a média . digite 0 (zero para terminar)")   
while True:
    valor=float(input("digite um número"))
    if valor ==0:
         break
    soma +=valor
    contador  += 1
    if contador==-0:
       print("nenhum numero foi inserido.")
    else:
       media =soma/contador
       print("a media dos numeros inseridos é:", media)
