import pygame as p

p.font.init()
width = height = 600
dim = 3
sqsize = height // dim
maxfps = 5
images = {}
WINNER_FONT = p.font.SysFont('comicsans', 100)
WHITE = (255, 255, 255)
screen = p.display.set_mode((width, height))


class GameState:
    def __init__(self):
        self.board = [
            ["--", "--", "--"],
            ["--", "--", "--"],
            ["--", "--", "--"]
        ]


def loadImages():
    pieces = ["cross", "circle"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("image/" + piece + ".png"), (sqsize - 10, sqsize - 10))


def main():
    p.init()
    clock = p.time.Clock()
    screen.fill(WHITE)
    loadImages()
    gs = GameState()
    running = True
    current_piece = "circle"
    drawGameState(screen, gs)
    move_count = 0
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // sqsize
                row = location[1] // sqsize
                sqselected = (row, col)
                if gs.board[row][col] == "--":
                    gs.board[row][col] = current_piece
                    if current_piece == "circle":
                        current_piece = "cross"
                    else:
                        current_piece = "circle"
                    drawGameState(screen, gs)
                    move_count += 1
                    if move_count > 4:
                        if containTriple(gs.board):
                            if current_piece == "circle":
                                result("Cross Wins!")
                            else:
                                result("Circle Wins!")
                        elif move_count == 9:
                            result("It's a tie!")

        clock.tick(maxfps)
        p.display.update()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colour = (0, 0, 0)
    for r in range(dim + 1):
        p.draw.rect(screen, colour, p.Rect(width * r//3 - 5, 0, 10, height))
    for c in range(dim + 1):
        p.draw.rect(screen, colour, p.Rect(0, height * c//3 - 5, width, 10))


def drawPieces(screen, board):
    for r in range(dim):
        for c in range(dim):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c * sqsize + 5, r * sqsize + 5, sqsize, sqsize))


def containTriple(board):
    if board[2][2] != "--" and (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]):
        return True
    for i in range(dim):
        if "--" != board[i][0] == board[i][1] == board[i][2] or "--" != board[2][i] == board[1][i] == board[0][i]:
            return True


def result(text):
    draw_text = WINNER_FONT.render(text, False, (125, 125, 125))
    screen.blit(draw_text, (width/2 - draw_text.get_width() /
                         2, height/2 - draw_text.get_height()/2))
    p.display.update()
    p.time.delay(5000)
    main()


main()
