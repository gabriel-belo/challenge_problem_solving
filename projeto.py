continuar=""
cont_carros=0
lista=[]
def calculo_tempo(deslocamento:int, velocidade_media:int)->int:
    tempo = deslocamento/velocidade_media
    lista.append(tempo)
    del tempo
    return lista

deslocamento=int(input("Qual a distância de deslocamento metros: "))

while "N" not in continuar:
    velocidade_kmph=int(input("Velocidade média em km/h: "))
    velocidade_mpm = (velocidade_kmph * 1000) / 60
    cont_carros+=1
    continuar=input("Gostaria de continuar[S/N]: ").upper().split()
    a= calculo_tempo(deslocamento, velocidade_mpm)

# for elemento in lista:
#     total+= elemento
# media= total / cont_carros
media = sum(lista) / len(lista)
print(lista)
print(f"Passaram {cont_carros} carros ")
print(f"A média de tempo gasto pelos carros é {media:.2f}")