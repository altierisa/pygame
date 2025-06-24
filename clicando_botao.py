import pygame

pygame.init() #inicializa o pygame
largura = 800 #define largura
altura = 600 #define altura
fonte = pygame.font.SysFont(None, 36)

tela = pygame.display.set_mode((largura, altura))

def desenhar_botao(texto,posicao,cor):
    texto_render = fonte.render(texto, True, (0,0,0))
    retangulo = texto_render.get_rect(center=posicao)
    pygame.draw.rect(tela, cor, retangulo.inflate(20, 20))
    tela.blit(texto_render, retangulo)
    return retangulo


rodando = True #variavel pra controlar o loop principal do game
while rodando:#loop principal do jogo
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(evento.pos):
                print("Botão clicado!")

    tela.fill((255,203,219)) #preenche a tela com ''rosa''
    botao = desenhar_botao("Clique aqui", (200, 150),(100,100,100)) #botao verde
    pygame.display.update() #atualiza a tela

pygame.quit() #encerra a tela