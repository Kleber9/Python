import random
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:48:52 2020

@author: kleber
"""

def jogar():
    print("Jogo da advinhação!")


    print("   /|")
    print("  /3|")
    print(" /11|")
    print("/777|")


    num_secreto = int(random.randrange(1, 101))
    tentativas = 1
    chances = 0
    pontos = 1000

    print("Digite o nível  que deseja jogar, sendo 1 - (Fácil), 2 - (Médio) e 3 - (Dificil)")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        chances = 10
    elif(nivel == 2):
        chances = 5
    else:
        chances = 3

 
    for tentativas in range(1,chances + 1):
        print(f"Tentativa {tentativas} de {chances}!")
        str_chute = input("Digite um numero entre 1 a 100: ")
        chute = int(str_chute)
    
        if(chute < 0):
            print("O número tem que ser de 1 a 100")
            continue
        elif(chute > 100):
            print("O número tem que ser menor que 100")
            continue
        acertou = chute == num_secreto
        maior   = chute >  num_secreto
        menor   = chute <  num_secreto
    
        if(acertou):
            print("Ganhou!")
            print(f"Total de pontos {pontos}")
            break
        else:
            if(maior):
                print("Maior")
            elif(menor):
                print("menor")
        pontos_perdidos = abs(round(num_secreto - chute / 3))  
        print(pontos_perdidos)
        pontos -= pontos_perdidos       
        tentativas += tentativas
    
    
    print(f"O número secreto era: {num_secreto}!")    
    print(f"Você ficou com {pontos} pontos")    
    print("Fim do jogo!")   

if(__name__ =="__main__"):    
    jogar()