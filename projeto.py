continuar=""
cont_carros=0
media=0

def calculo_tempo(deslocamento:int, velocidade_média:int, total:int)->int:
    tempo = deslocamento/velocidade_média
    total+= tempo
    return total

deslocamento=int(input("Qual a distância de deslocamento: "))
while "N" not in continuar:
    velocidade_media=int(input("Velocidade média em km/h: "))
    cont_carros+=1
    continuar=input("Gostaria de continuar: ")
    a= calculo_tempo(deslocamento, velocidade_media)
    

t= calculo_tempo(total=int)
media= t / cont_carros

print(f"Passaram {cont_carros} carros ")
print(f"A média de tempo gasto pelos carros é {media}")