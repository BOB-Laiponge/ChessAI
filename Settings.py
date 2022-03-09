class Settings:
    def __init__(self, board_width):
        self.always_hoover = True
        self.board_width = self._check_board_width(board_width)
        self.box_width = board_width // 8

    def _check_board_width(self, board_width):
        error = board_width % 8
        if error != 0 :
            board_width = board_width - error
            print(f"WARNING : Board Width not divisible by 8. Changed to {board_width}")

        return board_width



