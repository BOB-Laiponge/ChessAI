import pygame
from constants import PIECES_DICT, COLOR_DICT


class Piece:
    def __init__(self, engine, type, position):
        self.engine = engine
        self.position_on_board = position # [i,j]
        self.position_on_screen = []
        self.update_position_on_screen() # [x,y]
        self.type = type
        self.image = engine.pieces_images.get(type)
        self.stick_to_mouse = False

        self.legal_moves = []

    def get_image(self):
        return self.image

    def get_type(self):
        return self.type

    def update_position_on_screen(self):
        self.position_on_screen = (
            self.position_on_board[1] * self.engine.settings.box_width,
            self.position_on_board[0] * self.engine.settings.box_width
        )

    def move(self, new_pos):
        self.position_on_board = new_pos
        self.update_position_on_screen()

    def inverse_som(self):
        self.stick_to_mouse = not self.stick_to_mouse
