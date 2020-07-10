

class Piece:

    def __init__(self, type, row, col, color):

        # Types:
        # pawn
        # knight
        # bishop
        # rook
        # queen
        # king
        self.type = type

        if self.type == 'rook' or self.type == 'king':
            self.castle_conditions = True

        if self.type == 'king':
            self.can_castle_left = False
            self.can_castle_right = False

        self.row = row
        self.col = col

        # white = 0
        # black = 1
        self.color = color

    def possible_moves(self, board):
        moves = []

        if self.type == "pawn":
            if self.color == 0:
                # white player
                moves.append([self.row + 1, self.col]) # Move forward
                moves.append([self.row + 1, self.col - 1]) # Move left
                moves.append([self.row + 1, self.col + 1]) # Move right
            else:
                # black player
                moves.append([self.row - 1, self.col])
                moves.append([self.row - 1, self.col - 1])
                moves.append([self.row - 1, self.col + 1])
        elif self.type == "knight":
            moves.append([self.row + 2, self.col - 1])
            moves.append([self.row + 2, self.col + 1])
            moves.append([self.row - 2, self.col + 1])
            moves.append([self.row - 2, self.col - 1])
            moves.append([self.row - 2, self.col + 1])
            moves.append([self.row - 1, self.col + 2])
            moves.append([self.row + 1, self.col + 2])
            moves.append([self.row + 1, self.col - 2])
            moves.append([self.row - 1, self.col - 2])
        elif self.type == "bishop":
            for i in range(7):
                moves.append([self.row + i, self.col + i])
                moves.append([self.row - i, self.col - i])
        elif self.type == "rook":
            for i in range(7):
                moves.append([self.row + i, self.col])
                moves.append([self.row - i, self.col])
                moves.append([self.row, self.col + i])
                moves.append([self.row, self.col - i])
        elif self.type == "queen":
            for i in range(7):
                moves.append([self.row + i, self.col])
                moves.append([self.row - i, self.col])
                moves.append([self.row, self.col + i])
                moves.append([self.row, self.col - i])
                moves.append([self.row + i, self.col + i])
                moves.append([self.row - i, self.col - i])
        elif self.type == "king":
            self.can_castle_left = False
            self.can_castle_right = False

            moves.append([self.row + 1, self.col])
            moves.append([self.row - 1, self.col])
            moves.append([self.row, self.col + 1])
            moves.append([self.row, self.col - 1])
            moves.append([self.row + 1, self.col + 1])
            moves.append([self.row - 1, self.col - 1])

        # Filter out moves that are outside of the space
        for move in moves:

            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                moves.remove(move)

        # Filter out moves that conflict with own pieces
        for move in moves:

            if board[move[0]][move[1]].color == self.color:
                # If the board contains a piece of the same color, remove that move
                moves.remove(move)

        # CASTLING!!
        if self.type == 'king':
            [self.can_castle_left, self.can_castle_right] = board.check_castle_conditions(self.color)

    def numcol2alph(self):

        if self.col == 0:
            return 'a'
        elif self.col == 1:
            return 'b'
        elif self.col == 2:
            return 'c'
        elif self.col == 3:
            return 'd'
        elif self.col == 4:
            return 'e'
        elif self.col == 5:
            return 'f'
        elif self.col == 6:
            return 'g'
        elif self.col == 7:
            return 'h'

    def check_type(self, test_type):

        if test_type == 'p' and self.type == "pawn" and self.color == 0:
            return True
        elif test_type == 'P' and self.type == "pawn" and self.color == 1:
            return True
        elif test_type == 'n' and self.type == "knight" and self.color == 0:
            return True
        elif test_type == 'N' and self.type == "knight" and self.color == 1:
            return True
        elif test_type == 'b' and self.type == "bishop" and self.color == 0:
            return True
        elif test_type == 'B' and self.type == "bishop" and self.color == 1:
            return True
        elif test_type == 'r' and self.type == "rook" and self.color == 0:
            return True
        elif test_type == 'R' and self.type == "rook" and self.color == 1:
            return True
        elif test_type == 'q' and self.type == "queen" and self.color == 0:
            return True
        elif test_type == 'Q' and self.type == "queen" and self.color == 1:
            return True
        elif test_type == 'k' and self.type == "king" and self.color == 0:
            return True
        elif test_type == 'K' and self.type == "king" and self.color == 1:
            return True
        else:
            return False

    def __str__(self, full=False):
        if not full:
            if self.type is None:
                return "."
            elif self.type == "pawn" and self.color == 0:
                return "p"
            elif self.type == "knight" and self.color == 0:
                return "n"
            elif self.type == "bishop" and self.color == 0:
                return "b"
            elif self.type == "rook" and self.color == 0:
                return "r"
            elif self.type == "queen" and self.color == 0:
                return "q"
            elif self.type == "king" and self.color == 0:
                return "k"

            elif self.type == "pawn" and self.color == 1:
                return "P"
            elif self.type == "knight" and self.color == 1:
                return "N"
            elif self.type == "bishop" and self.color == 1:
                return "B"
            elif self.type == "rook" and self.color == 1:
                return "R"
            elif self.type == "queen" and self.color == 1:
                return "Q"
            elif self.type == "king" and self.color == 1:
                return "K"

        else:

            if self.type is None:
                return "."
            elif self.type == "pawn" and self.color == 0:
                return "p" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "knight" and self.color == 0:
                return "n" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "bishop" and self.color == 0:
                return "b" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "rook" and self.color == 0:
                return "r" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "queen" and self.color == 0:
                return "q" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "king" and self.color == 0:
                return "k" + str(self.numcol2alph()) + str(self.row)

            elif self.type == "pawn" and self.color == 1:
                return "P" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "knight" and self.color == 1:
                return "N" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "bishop" and self.color == 1:
                return "B" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "rook" and self.color == 1:
                return "R" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "queen" and self.color == 1:
                return "Q" + str(self.numcol2alph()) + str(self.row)
            elif self.type == "king" and self.color == 1:
                return "K" + str(self.numcol2alph()) + str(self.row)