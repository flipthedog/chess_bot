from Board import Board

board = Board()

while not board.end:
    print('---- TURN', board.turn, ":----\n")
    print(board)
    print('---WHITE PIECES---')
    for piece in board.return_white_pieces():
        print(piece.__str__(True))
    print('---BLACK PIECES---')
    for piece in board.return_black_pieces():
        print(piece.__str__(True))

    input("Enter your move: ")