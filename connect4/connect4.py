import numpy as np
import pygame


ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)


def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def print_board(board):
    print(np.flip(board, 0))


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, (0, 0, 0), (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                   int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COL_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (int(
                        c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, (255, 255, 0), (int(
                        c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()


def winning_move(board, piece):
        # Check horizontal locations for win
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


pygame.init()

board = create_board()
game_over = False
turn = 0

# making board for first time
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, (0, 0, 255), (0, SQUARESIZE,
                                       COL_COUNT * SQUARESIZE, ROW_COUNT * SQUARESIZE))
pygame.display.set_caption('Connect4')
draw_board(board)

myfont = pygame.font.SysFont('monospace', 75)

while not game_over:
    print_board(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, (255, 0, 0),
                                   (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, (255, 255, 0),
                                   (posx, int(SQUARESIZE / 2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))

            posx = event.pos[0]
            if turn == 0:
                col = posx // SQUARESIZE

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        label = myfont.render('player 1 wins', 1, (255, 0, 0))
                        screen.blit(label, (40, 10))
                        print('player 1 wins')
                        game_over = True

            else:
                col = posx // SQUARESIZE
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = myfont.render(
                            'player 2 wins', 1, (255, 255, 0))
                        screen.blit(label, (40, 10))
                        print('player 2 wins')
                        game_over = True
            turn += 1
            turn %= 2
            draw_board(board)
            print_board(board)
            if game_over:
                pygame.time.wait(3000)
