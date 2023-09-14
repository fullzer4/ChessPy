"""

"""

'''

'''

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Funcao para carregar imagens da pecas
loadImages():
    pieces = [ "pecas do tabuleiro" ]
    loop para carrega a imagem e botar na escala certa e carregar no tabuleiro
'''

def loadImages():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'Chess/Imgs/{piece}.png'), (SQ_SIZE, SQ_SIZE))
    
'''
Funcao para iniciar o tabuleiro
main():
    iniciar pygame
    inicar a tela
    iniciar o relogio
    setar o fundo como branco
    iniciar a engine do jogo
    carregar as imagens
    loop para rodar o jogo:
        desenhar o tabuleiro do jogo
        definir o FPS para futuras animacoes
        mostrar na tela
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running: 
        for e in p.event.get():
            if e.type == p.QUIT:
                running= False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if 0 <= col < 8 and 0 <= row < 8:
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        sqSelected = ()
                        playerClicks = []

                    
                
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
        
'''

'''

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
    
'''

'''
    
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
'''

'''
    
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()