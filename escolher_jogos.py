import adivinhacao
import forca
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:33:15 2020

@author: kleber
"""

def escolhe_jogo():
    print("Qual jogo quer jogar?")
    print(" 1 - *Jogo da Forca* ")
    print(" 2 - *Adivinhação*") 
    escolha = int(input("escolha: "))
    if(escolha == 1):    
        adivinhacao.jogar()    
    elif(escolha == 2):    
        forca.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()