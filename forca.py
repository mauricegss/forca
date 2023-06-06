import random
from re import search

palavras = ["helicoptero", "pelicano", "laranjeira", "cadeirante"]
escolha = random.choice(palavras)

display = []
for n in range(len(escolha)):
    display.append('_')
print(display)

vidas = 6

while vidas > 0 and "_" in display:
    chute = input("Digite Letra: ")
    cont = 0
    acertou = False
    for letra in escolha:
        if chute == letra:
            display[cont]=chute
            acertou=True
        cont += 1
    if not acertou:
        vidas -= 1
        print("Faltam",vidas,"vidas")
    print(display)

if vidas>0:
    print("Parabens!")
    print("A Palavra e "+escolha)
else:
    print("Perdeu!")
    print("A Palavra era "+escolha)
