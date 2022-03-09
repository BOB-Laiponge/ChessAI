class FEN_Translator:
    def __init__(self, board):
        self.board = board

    def import_from_fen(self, fen_str):
        self.board.clear_board()

        fen = fen_str.split()
        index_i = 0
        index_j = 0
        symb_digit = ['1', '2', '3', '4', '5', '6', '7', '8']

        for char in fen[0]:
            if char == '/':
                index_i += 1
                index_j = 0
            elif char in symb_digit:
                index_j += int(char)
            else:
                type = ""
                if char.islower():
                    type += "b"
                else:
                    type += "w"
                type += char.lower()
                self.board.place_piece_on_board((index_i, index_j), type)
                index_j += 1
