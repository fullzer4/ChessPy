import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the chess board
chess_board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Initialize Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load chess piece images
pieces = {
    'wp': pygame.image.load("wp.png"),
    'wr': pygame.image.load("wr.png"),
    'wn': pygame.image.load("wn.png"),
    'wb': pygame.image.load("wb.png"),
    'wq': pygame.image.load("wq.png"),
    'wk': pygame.image.load("wk.png"),
    'bp': pygame.image.load("bp.png"),
    'br': pygame.image.load("br.png"),
    'bn': pygame.image.load("bn.png"),
    'bb': pygame.image.load("bb.png"),
    'bq': pygame.image.load("bq.png"),
    'bk': pygame.image.load("bk.png")
}

# Initialize the game state
selected_piece = None
turn = 'w'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

            if selected_piece is None:
                piece = chess_board[row][col]
                if piece is not None and piece.startswith(turn):
                    selected_piece = (row, col)
            else:
                target_piece = chess_board[row][col]
                if (row, col) != selected_piece and target_piece is not None and target_piece.startswith(turn):
                    selected_piece = (row, col)
                else:
                    chess_board[row][col] = chess_board[selected_piece[0]][selected_piece[1]]
                    chess_board[selected_piece[0]][selected_piece[1]] = None
                    selected_piece = None
                    turn = 'b' if turn == 'w' else 'w'

    # Draw the board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = chess_board[row][col]
            if piece is not None:
                img = pieces[piece]
                window.blit(img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
