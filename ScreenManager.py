import pygame

from constants import LIGHT_BROWN, DARK_BROWN


class ScreenManager:
    def __init__(self, engine):
        self.screen = None
        self.engine = engine

        self.box_width = self.engine.settings.box_width

    def init_screen(self):
        self.screen = pygame.display.set_mode((self.engine.settings.board_width, self.engine.settings.board_width))
        pygame.display.set_caption("Chess")

    def get_screen(self):
        return self.screen

    def update_screen(self):
        pos = self.engine.mouse_pos_on_screen
        pos_on_board = self.engine.mouse_pos_on_board

        # Draw background
        self._draw_background([LIGHT_BROWN, DARK_BROWN])

        # Draw hoover
        self._draw_hoover((0, 0, 255), pos_on_board)

        # Draw selection
        if self.engine.selected != None:
            self._draw_selection()

        # Draw pieces
        self._draw_pieces(pos)

        # Update screen
        pygame.display.flip()

    def _draw_background(self, colors):
        """Draws background """
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen, colors[(i + j) % 2],
                                 pygame.Rect(i * self.box_width, j * self.box_width,
                                             self.box_width, self.box_width))

    def _draw_hoover(self, color, pos_on_board):
        """ Draw the rectangle around a box when the mouse hoovers it"""
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(pos_on_board[1] * self.box_width,
                                     pos_on_board[0] * self.box_width,
                                     self.box_width, self.box_width), 4)

    def _draw_selection(self):
        """ Draw the rectangle around a box when selected """
        x, y = self.engine.selected.position_on_screen
        pygame.draw.rect(self.screen, (255, 0, 0),
                         pygame.Rect(x, y,
                                     self.box_width, self.box_width), 4)

    def _draw_pieces(self, pos):
        """ Draw the chess pieces. If one piece is selected, it will stick to the mouse """
        delta = self.box_width // 2
        tmp = []

        for piece in self.engine.board.get_pieces_list():
            if piece.stick_to_mouse:
                tmp.append(piece)
            else:
                self.screen.blit(piece.image, piece.position_on_screen)

        for piece in tmp:
            self.screen.blit(piece.image, (pos[0] - delta, pos[1] - delta))
