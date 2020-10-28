import random
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:26:24 2020

@author: kleber
"""



def jogar():
    
    apresentacao()                
    palavra_secreta = gera_palavra()    
    letras_corretas = verifica_tamanho_palavra(palavra_secreta)
 
    enforcou = False
    acertou = False
    
    erros = 0 

    print(palavra_secreta)
    print(letras_corretas)
    
    #Inicio do game_loop
    while(not enforcou and not acertou):
        chute = ver_chute()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.lower() == letra.lower()):
                    letras_corretas[index]  = letra
                    print("A palavra {} existe e está na posição {} da palavra secreta" . format(chute,index))
                    print(letras_corretas)
                    if("_" not in letras_corretas):
                        print("GANHOU!")
                        acertou = True
                index += 1                                    

        else:            
            erros += 1
            verifica_erros(erros)
            if(erros == 6):
                enforcou = True
            
            
    
    
    finaliza_jogo()
    
    
def apresentacao():
    print ("Bem vindo ao jogo da forca!")
    print( "_______")
    print("|      '")
    print("|      '")
    print("|      O")
    print("|    --|--")
    print("|     / \ ")

def gera_palavra():
    arquivo = open("C:/Users/Kleber/Desktop/ESTUDOS/Python/palavras.txt","r")
    palavras = []
    
    
    for linha in arquivo:        
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    num = random.randrange(0,len(palavras))
    palavra_secreta = palavras[num].lower()
    return palavra_secreta

def verifica_tamanho_palavra(palavra_secreta):
    return ["_" for cada_letra in palavra_secreta]

def ver_chute():
    return input("Qual a letra: ").strip().lower()

def finaliza_jogo():
    return print("Fim de jogo!")

def verifica_erros(erros):
    if(erros == 1):
        print("{}º erro" . format(erros))
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
    elif(erros == 2):
        print("{}º erro" . format(erros))
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
        print("|      |")
    elif(erros == 3):
        print("{}º erro" . format(erros))
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
        print("|      |--")
    elif(erros == 4):
        print("{}º erro" . format(erros))
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
        print("|    --|--")
    elif(erros == 5):
        print("{}º e ultima tentativa" . format(erros))
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
        print("|    --|--")
        print("|       \ ")
    else:
        print( "_______")
        print("|      '")
        print("|      '")
        print("|      O")
        print("|    --|--")
        print("|     / \ ")
        

    
if(__name__ =="__main__"):    
    jogar()