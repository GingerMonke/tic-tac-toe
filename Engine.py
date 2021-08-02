import math
from copy import deepcopy

tries = 0

class Board:

    def __init__(self):
        self.cells = [
            ["--", "--", "--"],
            ["--", "--", "--"],
            ["--", "--", "--"]
        ]
        self.current_piece = "circle"

    def is_circle_move(self):
        return self.current_piece == "circle"

    def make_move(self, move):
        new = deepcopy(self)
        new.cells[move[0]][move[1]] = new.current_piece
        new.current_piece = "cross" if new.is_circle_move() else "circle"
        return new

    def has_triple(self):
        if self.cells[1][1] != "--" and (self.cells[0][0] == self.cells[1][1] == self.cells[2][2] or (
                self.cells[2][0] == self.cells[1][1] == self.cells[0][2])):
            return True

        for i in range(3):
            if "--" != self.cells[i][0] == self.cells[i][1] == self.cells[i][2] or (
                    "--" != self.cells[2][i] == self.cells[1][i] == self.cells[0][i]):
                return True

    def is_draw(self):
        if len(self.get_all_moves()) == 0 and not self.has_triple():
            return True

    def get_all_moves(self):
        # initialising the move list
        moves = []
        # going through each element in the list
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                if self.cells[r][c] == "--":
                    moves.append((r, c))
        return moves

    def is_over(self):
        return self.has_triple() or self.is_draw()


class Opponent:

    def minimax(self, board, depth, a, b):
        if depth == 0 or board.is_over():
            return self.evaluate(board)
        if board.is_circle_move():
            best = -math.inf
            for move in board.get_all_moves():
                evaluation = self.minimax(board.make_move(move), depth - 1, a, b)
                best = max(best, evaluation)
                a = max(a, evaluation)
                if b <= a:
                    break
        else:
            best = math.inf
            for move in board.get_all_moves():
                evaluation = self.minimax(board.make_move(move), depth - 1, a, b)
                best = min(best, evaluation)
                b = min(b, evaluation)
                if b <= a:
                    break
        return best

    def get_best_move(self, board, depth):
        moves = board.get_all_moves()
        best_move = " "
        best_value = -math.inf if board.is_circle_move() else math.inf
        for move in moves:
            value = self.minimax(board.make_move(move), depth, -math.inf, math.inf)
            if (board.is_circle_move() and value > best_value) or (
                    not board.is_circle_move() and value < best_value):
                best_value = value
                best_move = move
        return best_move

    def evaluate(self, board):
        global tries
        tries += 1
        print(tries)
        if board.has_triple():
            return 1 if not board.is_circle_move() else -1
        return 0

    # def minimax(self, board, depth):
    #     if depth == 0 or board.is_over():
    #         return self.evaluate(board)
    #     if board.is_circle_move():
    #         return self.evaluate_outcomes(board, -math.inf, max, depth)
    #     else:
    #         return self.evaluate_outcomes(board, math.inf, min, depth)
    #
    # def evaluate_outcomes(self, board, worst, best_of, depth):
    #     best = worst
    #     for move in board.get_all_moves():
    #         evaluation = self.minimax(board.make_move(move), depth - 1)
    #         best = best_of(best, evaluation)
    #     return best
    #
    # def get_best_move(self, board, depth):
    #     moves = board.get_all_moves()
    #     best_move = " "
    #     best_value = -math.inf if board.is_circle_move() else math.inf
    #     for move in moves:
    #         value = self.minimax(board.make_move(move), depth)
    #         if (board.is_circle_move() and value > best_value) or (
    #                 not board.is_circle_move() and value < best_value):
    #             best_value = value
    #             best_move = move
    #     return best_move