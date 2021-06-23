import math
from copy import deepcopy


class GameState():
    def __init__(self):
        # board is 8x8 2D List, each element of the list has 2 characters
        # initial character == colour (b,w)
        # second character == piece
        # R == rook, N == knight, B == bishop, Q == Queen, K == king, P == pawn
        # -- == empty space
        self.board = [
            ["--", "--", "--"],
            ["--", "--", "--"],
            ["--", "--", "--"]
        ]

        self.whiteToMove = True
        self.moveLog = []


class Move():
    rankToRows = {"1": 4, "2": 3, "3": 2, "4": 1, "5": 0}
    rowToRanks = {v: k for k, v in rankToRows.items()}
    fileToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    colsToFile = {v: k for k, v in fileToCols.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[0]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]