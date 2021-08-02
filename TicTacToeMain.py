import pygame as p
import Engine
p.font.init()
width = height = 600
dim = 3
sqsize = height // dim
maxfps = 5
images = {}
WINNER_FONT = p.font.SysFont('comicsans', 100)
WHITE = (255, 255, 255)
screen = p.display.set_mode((width, height))


def load_images():
    pieces = ["cross", "circle"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("image/" + piece + ".png"), (sqsize - 10, sqsize - 10))


def main():
    p.init()
    clock = p.time.Clock()
    screen.fill(WHITE)
    load_images()
    board = Engine.Board()
    opp = Engine.Opponent()
    global running
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // sqsize
                row = location[1] // sqsize
                selected_sq = (row, col)
                if board.is_circle_move():
                    if board.cells[row][col] == "--":
                        board = board.make_move(selected_sq)

        if board.has_triple():
            if not board.is_circle_move():
                result("Circle Wins!")
            else:
                result("Cross Wins!")
        if board.is_draw():
            result("It's a tie!")
        elif not board.is_circle_move():
            move = opp.get_best_move(board, 5)
            board = board.make_move(move)

        draw_game_state(screen, board)
        clock.tick(maxfps)
        p.display.update()


def draw_game_state(screen, board):
    draw_board(screen)
    draw_pieces(screen, board.cells)


def draw_board(screen):
    colour = (0, 0, 0)
    for r in range(dim + 1):
        p.draw.rect(screen, colour, p.Rect(width * r//3 - 5, 0, 10, height))
    for c in range(dim + 1):
        p.draw.rect(screen, colour, p.Rect(0, height * c//3 - 5, width, 10))


def draw_pieces(screen, board):
    for r in range(dim):
        for c in range(dim):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c * sqsize + 5, r * sqsize + 5, sqsize, sqsize))


def result(text):
    print(text)
    global running
    running = False


main()