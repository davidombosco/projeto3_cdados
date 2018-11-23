# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:03:27 2018

@author: Bruno Sanches
"""



import pygame
import pyganim
from random import randrange
import numpy as np
import pandas as pd
import random



pygame.init()
#configurações iniciais
tela = pygame.display.set_mode((700,700), 0, 32)
tela.fill((0,0,0))
tabela=pd.read_excel('Projeto3.xlsx')
#TELA
myfont = pygame.font.SysFont('Calibri',56)

gostei=0
contador=0

fundo=pygame.image.load('fundo.png')
deu_like=pygame.image.load('like.png')
deu_dislike=pygame.image.load('dislike.png')
intermediaria=pygame.image.load('intermediario.png')
final=pygame.image.load('final.png')
#numero_gostei = myfont.render(str(gostei),1,(0,0,0))
#gif
animObj = pyganim.PygAnimation([('1.png', 700), ('2.png', 700)])
animObj.play()
mainclock=pygame.time.Clock()
meninas_liked=[]

carregar=True
gif=True
#carregar fotos    
while carregar:
    menina = ['img_utilizaveis/'+str(image)+'.png' for image in range(340)] #lista
    #while gif:
     #animação
       
       
    for i in range(340):
        menina[i]=pygame.image.load(str(menina[i]))
        print(i)
        animObj.blit(tela, (0,0))
        mainclock.tick(30)
        pygame.display.update()
    
    
    carregar=False
    gif=False
   
  


like=[]
k=random.randint(0,1)
if k==0:
    primeiras_15=[10,65,158,57,78,93,94,170,244,84,89,122,3,64,101]
else:
    primeiras_15=[18,133,280,118,126,129,131,175,52,123,136,152,153,147,151]
dislike=[]
contador=0

game_over=False
contador_inicial=0
rodando=True
JAJA=0
while rodando:
    
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            rodando = False
            
        
    if contador_inicial<15:
        
        tela.blit(fundo,(0,0))
        tela.blit(menina[primeiras_15[contador_inicial]],(100,100))   #indices iniciais
        pygame.time.delay(80)
        pygame.display.update()
        
        for event in pygame.event.get():
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                like.append(tabela.SpectralClustering[primeiras_15[contador_inicial]])
                print('like')
                contador_inicial+=1
                tela.blit(deu_like,(0,0))
                pygame.time.delay(50)
                pygame.display.update()
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                dislike.append(tabela.SpectralClustering[primeiras_15[contador_inicial]])
                print('dislike')
                contador_inicial+=1  
                tela.blit(deu_dislike,(0,0))
                pygame.time.delay(50)
                pygame.display.update()
            

            if event.type == pygame.QUIT:
                rodando = False
                     
    
    elif contador<len(menina):
        while JAJA<=7:
            tela.blit(intermediaria,(0,0)) 
            pygame.time.delay(500)
            pygame.display.update()
            JAJA+=1
        
     
        tela.blit(fundo,(0,0))
        tela.blit(menina[contador],(100,100))
        pygame.time.delay(20)
        pygame.display.update()
        
        if tabela.SpectralClustering[contador] in like:
            print('like')
            gostei+=1
            meninas_liked.append('like')
            contador+=1
            tela.blit(deu_like,(0,0))
            pygame.time.delay(50)
            pygame.display.update()
            
        elif tabela.SpectralClustering[contador] in dislike:
            print('dislike')
            meninas_liked.append('dislike')
            contador+=1
            tela.blit(deu_dislike,(0,0))
            pygame.time.delay(50)
            pygame.display.update()
         
    else:
        game_over=True
        print(meninas_liked)
                
            
    while game_over:
        tela.blit(final,(0,0))
        numero_gostei = myfont.render(str(gostei),1,(255,255,255))
        tela.blit(numero_gostei,(70,346))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                contador=0
                contador_inicial=0
                like=[]
                dislike=[]
                game_over=False
                JAJA=0
                gostei=0
                meninas_liked=[]
                
            elif event.type == pygame.QUIT:
                game_over=False
                rodando=False
    
    
                
pygame.display.quit()
print(like)
print(dislike)



'''
coisas a fazer:

1-pegar algumas imagens de diferentes clusters
2-usuário dar like ou nao nas imagens
3-ver qual foram os clusteres q tiveram mais likes

4-python rodar automaticamente conforme os likes da pessoas (ver a qual cluster a ft pertence e se a pessoa gosta
do cluster)


'''



#4:
'''
if menina[contador] in (cluster que a pessoa deu mais like):
    like.append(menina[contador])
    #tela.blit(YEP,(20,10))
    print('like')
    contador+=1
    
elif menina[contador] in (cluster que a pessoa deu menos like):
    dislike.append(menina[contador])
    #tela.blit(YEP,(20,10))
    print('dislike')
    contador+=1

'''