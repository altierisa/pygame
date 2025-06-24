import pygame
pygame.init() #inicializa o pygame

largura = 800 #define largura
altura = 600 #define altura

tela = pygame.display.set_mode((largura, altura)) #cria a tela com as dimensoes especificadas
pygame.display.set_caption("Exemplo de Jogo") #define o titulo da janela
rodando = True #variavel pra controlar o loop principal do game
while rodando:#loop principal do jogo
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255,255,255)) #preenche a tela com preto
    pygame.display.update() #atualiza a tela

pygame.quit() #encerra a tela
