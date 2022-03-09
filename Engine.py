import sys

import pygame

from EventHandler import EventHandler
from ScreenManager import ScreenManager
from board import Board
from constants import WHITE, LIGHT_BROWN, DARK_BROWN
from Settings import Settings


class Engine:
    def __init__(self):
        pygame.init()

        # Init settings
        self.settings = Settings(board_width=1000)
        print("Init : Settings")

        # Handlers and managers
        self.screen_manager = ScreenManager(self)
        print("Init : Screen Manager")
        self.event_handler = EventHandler(self)
        print("Init : Event Handler")
        self.board = Board(self)
        print("Init : Board")

        # Screen init
        self.screen_manager.init_screen()
        print("Init : Screen(init)")
        self.screen = self.screen_manager.get_screen()

        # Images loading
        self.pieces_images = self._load_images()

        # Other variables
        self.run = True
        self.selected = None
        self.mouse_pos_on_screen = self.event_handler.pos
        self.mouse_pos_on_board = self.event_handler.pos_on_board
        print("End Init")

    def start_game(self):
        self.board.start_new_game()
        self.mainloop()

    def mainloop(self):
        """Game's mainloop"""
        while self.run:
            # Update variables
            self.update_mouse()

            # check events
            self.event_handler.check_events()

            # Update screen
            self.screen_manager.update_screen()



    def _load_images(self):
        ### TO BE IMPROVED
        images = {
            "bk": pygame.transform.scale(pygame.image.load("images/kdt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "bq": pygame.transform.scale(pygame.image.load("images/qdt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "bb": pygame.transform.scale(pygame.image.load("images/bdt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "bn": pygame.transform.scale(pygame.image.load("images/ndt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "bp": pygame.transform.scale(pygame.image.load("images/pdt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "br": pygame.transform.scale(pygame.image.load("images/rdt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wk": pygame.transform.scale(pygame.image.load("images/klt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wq": pygame.transform.scale(pygame.image.load("images/qlt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wb": pygame.transform.scale(pygame.image.load("images/blt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wn": pygame.transform.scale(pygame.image.load("images/nlt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wp": pygame.transform.scale(pygame.image.load("images/plt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width)),
            "wr": pygame.transform.scale(pygame.image.load("images/rlt45.svg").convert_alpha(),
                                         (self.settings.box_width, self.settings.box_width))
        }

        return images

    def break_loop(self):
        self.run = False

    def select(self, pos):
        i, j = pos[0], pos[1]
        self.selected = self.board.get_piece(i, j)
        self.selected.inverse_som()

    def unselect(self):
        if self.selected != None: self.selected.inverse_som()
        self.selected = None

    def update_mouse(self):
        self.event_handler.update_mouse()
        self.mouse_pos_on_screen = self.event_handler.pos
        self.mouse_pos_on_board = self.event_handler.pos_on_board


