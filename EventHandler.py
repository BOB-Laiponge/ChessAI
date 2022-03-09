import sys

import pygame


class EventHandler:
    def __init__(self, engine):
        self.engine = engine
        self.pos = []
        self.pos_on_board = []

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # LEFT
                self.on_left_mouse_button_down()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # LEFT
                self.on_left_mouse_button_up()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right
                self.engine.unselect()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.engine.board.start_new_game()

    def on_left_mouse_button_down(self):
        if self.engine.selected == None and self.engine.board.get_piece(self.pos_on_board[0], self.pos_on_board[1]):
            self.engine.select(self.pos_on_board)
            self.engine.selected.mouse_delta = [self.pos[0] - self.pos_on_board[1] * self.engine.settings.box_width,
                                                self.pos[1] - self.pos_on_board[0] * self.engine.settings.box_width]
            print(self.engine.selected.mouse_delta)

    def on_left_mouse_button_up(self):
        if self.engine.selected != None:
            self.engine.board.move(self.engine.selected, self.pos_on_board)
        self.engine.unselect()

    def update_mouse(self):
        self.pos = pygame.mouse.get_pos()
        self.pos_on_board = self._get_pos_on_board(self.pos)

    def _get_pos_on_board(self, mouse_pos):
        x, y = mouse_pos[0], mouse_pos[1]
        x //= self.engine.settings.box_width
        y //= self.engine.settings.box_width
        return (y, x)
