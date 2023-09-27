import Chess.ChessMain as CH
import pygame as p

def startScreen():
    p.init()
    start_screen = p.display.set_mode((1280, 820))  
    start_button = p.image.load('./a.jpeg')
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (start_screen.get_width() // 2, start_screen.get_height() // 2)
    
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    running = False  
                    
        start_screen.fill(p.Color("white"))
        start_screen.blit(start_button, start_button_rect)
        p.display.flip()

    p.quit()

if __name__ == "__main__":
    startScreen()
    CH.main()