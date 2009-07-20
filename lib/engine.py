# -*- encoding: utf-8 -*-

class Board:
    def __init__(self):
        self.board = []

PIECE_L, PIECE_O, PIECE_T, PIECE_S, PIECE_Z, PIECE_J, PIECE_L = range(7)

class Piece:
    def __init__(self, letter):
        self.letter = letter