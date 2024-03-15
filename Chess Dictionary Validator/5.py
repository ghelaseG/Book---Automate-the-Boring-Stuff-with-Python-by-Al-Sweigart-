board = {'e3': 'wking', 'c6': 'wqueen',
         'g2': 'bbishop', 'd2': 'bqueen', 'g3': 'bking',
         'a1': 'bpawn', 'm1': 'bpawn', 'c1': 'bpawn', 'd1': 'bpawn',
         'e1': 'bpawn', 'f1': 'bpawn', 'g1': 'bpawn', 'h1': 'bpawn',
         'e2': 'bpawn', 'a2': 'bpawn'}

def isValidChessBoard(board):
    wKing, bKing, wPieces, bPieces = 0, 0, 0, 0
    wPawns, bPawns, spaces, check = 0, 0, [], True

    for x in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        for y in range(1,9):
            spaces.append(x + str(y))

        for space, piece in board.items():

            if space not in spaces:
                print('Space is wrong: ' + space + ' ' + piece)
                check = False
            if piece == 'wking':
                wKing += 1
            if piece == 'bking':
                bKing += 1
            if piece == 'wpawn':
                wPawns += 1
            if piece == 'bpawn':
                bPawns += 1
            if piece.startswith('w'):
                wPieces += 1
            if piece.startswith('b'):
                bPieces += 1

        if wKing != 1:
            print('While king != 1 : ' + str(wKing))
            check = False
        if bKing != 1:
            print('Black king != 1 : ' + str(bKing))
            check = False
        if wPieces > 16:
            print('Total white pieces on board > 16: ' + str(wPieces))
            check = False
        if bPieces > 16:
            print('Total black pieces on board > 16: ' + str(bPieces))
            check = False
        if wPawns > 8:
            print('White pawns on board > 8: ' + str(wPawns))
            check = False
        if bPawns > 8:
            print('Black pawns on board > 8: ' + str(bPawns))
            check = False

        if check:
            return True
        else:
            return False

    print(isValidChessBoard(board))
