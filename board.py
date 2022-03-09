from constants import STARTING_FEN
from fen_translator import FEN_Translator
from pieces.Piece import Piece


class Board:
    def __init__(self, engine):
        self.engine = engine
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.translator = FEN_Translator(self)

    def get_fen(self):
        pass

    def get_pieces_list(self):
        list = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    list.append((self.board[i][j]))
        return list

    def place_piece_on_board(self, pos, type):
        """
        :param pos: Position of the piece
        :param type: color char + type char
        """
        self.board[pos[0]][pos[1]] = Piece(self.engine, type, pos)

    def clear_board(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

    def start_new_game(self):
        self.translator.import_from_fen(STARTING_FEN)

    def move(self, piece, new_pos):
        old_pos = piece.position_on_board
        self.board[old_pos[0]][old_pos[1]] = 0
        self.board[new_pos[0]][new_pos[1]] = piece
        piece.move(new_pos)


    def get_piece(self, i, j):
        piece = self.board[i][j]
        if piece == 0:
            return None
        return piece


