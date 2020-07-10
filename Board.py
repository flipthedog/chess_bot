from Piece import Piece

class Board:

    def __init__(self):
        # Fill the board with empty cells
        self.board = [[Piece(None, -1, -1, -1) for i in range(8)] for j in range(8)]
        self.col = 8
        self.row = 8
        # self.board = [[Piece(None, -1, -1)]*8]*8
        self.create()
        self.end = False
        self.turn = 0

    def create(self):
        """
        Create the board and populate it
        :return:
        """

        for i in range(8):
            # Create white pawns
            self.board[1][i] = Piece("pawn", 1, i, 0)
            # Create black pawns
            self.board[6][i] = Piece("pawn", 6, i, 1)

            # Create white rooks
            self.board[0][0] = Piece("rook", 0, 0, 0)
            self.board[0][7] = Piece("rook", 0, 7, 0)

            # Create black rooks
            self.board[7][0] = Piece("rook", 7, 0, 1)
            self.board[7][7] = Piece("rook", 7, 7, 1)

            # Create white knights
            self.board[0][1] = Piece("knight", 0, 1, 0)
            self.board[0][6] = Piece("knight", 0, 6, 0)

            # Create black knights
            self.board[7][1] = Piece("knight", 7, 1, 1)
            self.board[7][6] = Piece("knight", 7, 6, 1)

            # Create white bishop
            self.board[0][2] = Piece("bishop", 0, 2, 0)
            self.board[0][5] = Piece("bishop", 0, 5, 0)

            # Create black bishop
            self.board[7][2] = Piece("bishop", 7, 2, 1)
            self.board[7][5] = Piece("bishop", 7, 5, 1)

            # Create white queen and king
            self.board[0][3] = Piece("queen", 0, 3, 0)
            self.board[0][4] = Piece("king", 0, 4, 0)

            # Create black queen and king
            self.board[7][3] = Piece("queen", 7, 3, 1)
            self.board[7][4] = Piece("king", 7, 4, 1)
    
    # Process a move for a player
    def move(self):
        pass
        # TODO

    def find_moves(self):

        if self.turn % 2 or self.turn == 0:
            # white player's turn
            pass
        else:
            # black player's turn
            pass

    def return_white_pieces(self):
        white_pieces = []
        for i in range(self.row):
            
            for j in range(self.col):
                
                if self.board[i][j].color == 0:
                    # White piece
                    white_pieces.append(self.board[i][j])
        
        return white_pieces
    
    def return_black_pieces(self):

        black_pieces = []
        for i in range(self.row):

            for j in range(self.col):

                if self.board[i][j].color == 1:
                    # is a black piece
                    black_pieces.append(self.board[i][j])
        
        return black_pieces

    def is_empty(self, cell):
        # Check if a cell is empty, return true/False

        return (cell.type == -1)

    # Check whether a particular player/color can castle
    def check_castle_conditions(self, color):
        
        if not color:
            # White player
            white_king = self.board[0][4]
            white_rook_1 = self.board[0][0]
            white_rook_2 = self.board[0][7]
            
            castle_left = False
            castle_right = False
            if white_king.type == 'king' and white_king.castle_conditions and white_rook_1 == 'rook' and \
                    white_rook_1.castle_conditions:
                if self.is_empty(self.board[0][1]) and self.is_empty(self.board[0][2]) and self.is_empty(self.board[
                                                                                                             0][3]):

                    castle_left = True

            if white_king.type == 'king' and white_king.castle_conditions and white_rook_2 == 'rook' and \
                    white_rook_2.castle_conditions:

                if self.is_empty(self.board[0][5]) and self.is_empty(self.board[0][6]):
                    castle_right = True

        else:
            # Black player
            
            black_king = self.board[0][4]
            black_rook_1 = self.board[0][0]
            black_rook_2 = self.board[0][7]

            castle_left = False
            castle_right = False

            if black_king.type == 'king' and black_king.castle_conditions and black_rook_1 == 'rook' and \
                    black_rook_1.castle_conditions:

                if self.is_empty(self.board[7][1]) and self.is_empty(self.board[7][2]) and self.is_empty(self.board[
                                                                                                             7][3]):
                    castle_left = True

            if black_king.type == 'king' and black_king.castle_conditions and black_rook_2 == 'rook' and \
                    black_rook_2.castle_conditions:

                if self.is_empty(self.board[7][5]) and self.is_empty(self.board[7][6]):

                    castle_right = True

        return [castle_left, castle_right]

    # Find a particular piece based on an entered command by the player
    # Format of command Ka6-a5
    def move_piece(self, move_command):

        if len(move_command) != 6:
            print("Invalid Move command")
        else:
            piece = move_command[0]
            home_square = move_command[1:2]
            Piece.numcol2alph()
            destination_square = move_command[4:5]

    # Convert an alphabet to a numeric column
    def alph2numcol(self, col):

        if col == 'a':
            return 0
        elif col == 'b':
            return 1
        elif col == 'c':
            return 2
        elif col == 'd':
            return 3
        elif col == 'e':
            return 4
        elif col == 'f':
            return 5
        elif col == 'g':
            return 6
        elif col == 'h':
            return 7
        else:
            return -1 # Invalid, return error value

    def __str__(self):
        return_string = "-----BOARD-----\n"
        return_string += "  a b c d e f g h \n"
        for i in range(self.row, 0, -1):
            return_string += str(i) + " "
            for j in range(self.col):
                return_string += (str(self.board[i - 1][j]) + " ")
            return_string += ("\n")
        return return_string