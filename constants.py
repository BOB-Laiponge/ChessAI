# By jurgenwesterhof (adapted from work of Cburnett) - http://commons.wikimedia.org/wiki/Template:SVG_chess_pieces, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=35634436

GREEN = (82, 137, 65)
WHITE = (220, 220, 210)
LIGHT_BROWN = (210, 185, 140)
DARK_BROWN = (100, 60, 0)

PIECES_DICT = {
    0: None,
    'k': "king",
    'p': "pawn",
    'b': "bishop",
    'n': "knight",
    'r': "rook",
    'q': "queen"
}
COLOR_DICT = {
    'w': "white",
    'b': "black"
}
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

MOVES = {
    "bk": [(1, 0), (0, 1)],
    "bq": [],
    "bb": [],
    "bn": [],
    "bp": [],
    "br": [],
    "wk": [],
    "wq": [],
    "wb": [],
    "wn": [],
    "wp": [],
    "wr": []
}
