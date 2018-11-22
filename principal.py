import pygame
import random
from personagem import Heroi, Bloco, Circulo
import time

LARGURA = 400
ALTURA = 700
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
vel=5
x=30
y=0



pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Torre")

listaSprites = pygame.sprite.Group()

heroi = Heroi(AZUL, 15, 15, 40, 40)

listaSprites.add(heroi)



amarelos = pygame.sprite.Group()       # blocos amarelos
circulos = pygame.sprite.Group()       #projeteis

chegada = Bloco(VERDE, LARGURA, 30, 0, ALTURA - 30 )
listaSprites.add(chegada)


projetil1=Circulo(20,100)
circulos.add(projetil1)

projetil2= Circulo(380,200)
circulos.add(projetil2)

projetil3 =Circulo(20,300)
circulos.add(projetil3)

projetil4 = Circulo(380,400)
circulos.add(projetil4)

projetil5 =Circulo(20,500)
circulos.add(projetil5)

projetil6 =Circulo(380,600)
circulos.add(projetil6)


listaSprites.add(circulos)

for i in range (40):

    x = random.randrange(LARGURA - 40)
    y = random.randrange(ALTURA - 60)
    blocoAmarelo = Bloco(AMARELO, 50, 10, x, y)
    blocoAmarelo.numero = i
    amarelos.add(blocoAmarelo)

listaSprites.add(amarelos)

font = pygame.font.Font(None, 36)
gameOver = False
sair = False
flag = False


while not sair:

    if projetil1.rect.x <= 400:
        projetil1.moverFrente(1)
        time.sleep(0.01)
    if projetil1.rect.x >= 400:
        projetil1.rect.x = 10

    if projetil2.rect.x >= 0:
        projetil2.moverTras(2)
    if projetil2.rect.x <= 0:
        projetil2.rect.x = 400

    if projetil3.rect.x <= 400:
        projetil3.moverFrente(2)
    if projetil3.rect.x >= 400:
        projetil3.rect.x = 10

    if projetil4.rect.x >= 0:
        projetil4.moverTras(1)
    if projetil4.rect.x <= 0:
        projetil4.rect.x = 400

    if projetil5.rect.x <= 400:
        projetil5.moverFrente(2)
    if projetil5.rect.x >= 400:
        projetil5.rect.x = 10

    if projetil6.rect.x >= 0:
        projetil6.moverTras(3)
    if projetil6.rect.x <= 0:
        projetil6.rect.x = 380

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sair =True


        tecla = pygame.key.get_pressed()



        if tecla[pygame.K_DOWN] and heroi.rect.y < 700 - vel - 20:
            heroi.cair()


        if tecla[pygame.K_UP] and heroi.rect.y > vel:

            heroi.subir()

        if tecla[pygame.K_RIGHT] and heroi.rect.x < 400 - vel - 20:
            heroi.andarDireita()

        if tecla[pygame.K_LEFT] and heroi.rect.x > vel:
            heroi.andarEsquerda()

    if pygame.sprite.spritecollideany(heroi, amarelos) or pygame.sprite.spritecollideany(heroi,circulos):
        heroi.rect.x= 30
        heroi.rect.y=30
        gameOver = False


    tela.fill(PRETO)
    listaSprites.draw(tela)
    pygame.display.update()

    chegou = pygame.sprite.collide_rect(heroi, chegada)
    if chegou == True:
        chegada.image.fill(VERMELHO)
        pygame.display.set_caption("Voce venceu")
        gameOver = True



pygame.quit()