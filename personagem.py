import pygame

vel = 10
HEIGHT= 20
WIDTH =20
RED =(255, 0, 0)

class Heroi (pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def subir(self):
        self.rect.y -= vel

    def cair(self):
        self.rect.y += vel

    def andarDireita(self):
        self.rect.x += vel

    def andarEsquerda(self):
        self.rect.x -= vel




class Bloco(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Circulo(pygame.sprite.Sprite):
    def __init__(self, x, y):  # posição x,y
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.rect = pygame.draw.circle(self.image, (255, 0, 0), (5, 5), 5)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moverFrente(self,velX):
        self.rect.x += velX

    def moverTras(self,velX):
        self.rect.x -= velX
