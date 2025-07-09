def rook_move(start_x, start_y, end_x, end_y):
    if start_x != end_x and start_y == end_y:
        return True
    elif start_y != end_y and start_x == end_x:
        return True
    else:
        return False

def king_move(start_x, start_y, end_x, end_y):
    # king moves anywhere, but must be one space
    # e.g (4,4) can move to (3,4), (5,4) | (4,5), (4,3)
    # diagonal -> (3,5), (3,3), (5,3), (5,5)
    # total of 8 valid moves
    x_difference = abs(start_x - end_x)
    y_difference = abs(start_y - end_y)

    # horizontal
    if x_difference == 1 and y_difference == 0:
        return True
    # vertical
    elif y_difference == 1 and x_difference == 0:
        return True
    # diagonal
    elif x_difference == 1 and y_difference == 1:
        return True
    else:
        return False

def bishop_move(start_x, start_y, end_x, end_y):
    # diagonal
    # e.g (4,4), valid -> (3,5), (2,6), (1,7) | upper left
    #                     (5,5), (6,6), (7,7), (8,8) | upper right
    #            lower -> (3,3), (2,2), (1,1) | left
    #                     (5,3), (6,2), (7,1) | right
    # differences between x and y must be equal

    x_difference = abs(start_x - end_x)
    y_difference = abs(start_y - end_y)

    if start_x == end_x and start_y == end_y:
        return False
    elif x_difference == y_difference:
        return True
    else:
        return False
def queen_move(start_x, start_y, end_x, end_y):
    if bishop_move(start_x, start_y, end_x, end_y) or rook_move(start_x, start_y, end_x, end_y):
        return True
    else:
        return False
'''
    # bishop movement
    if x_difference == y_difference:
        return True
    # rook movement
    elif start_x != end_x and start_y == end_y:
        return True
    elif start_y != end_y and start_x == end_x:
        return True
    else:
        return False
'''
def knight_move(start_x, start_y, end_x, end_y):
    # 8 valid moves
    # e.g (4,4) -> (3,6), (2,5), (2,3), (3,2), (5,2), (6,3), (6,5), (5,6)
    # if x moves 1, y must move 2, if x moves 2, y must move 1
    # moves 3 places

    x_difference = abs(start_x - end_x)
    y_difference = abs(start_y - end_y)

    if x_difference == 1 and y_difference == 2:
        return True
    elif x_difference == 2 and y_difference == 1:
        return True
    else:
        return False

def valid_chess_move(piece, start_x, start_y, end_x, end_y):
    is_valid = False
    if piece == "ROOK":
        is_valid = rook_move(start_x, start_y, end_x, end_y)
    elif piece == "KING":
        is_valid = king_move(start_x, start_y, end_x, end_y)
    elif piece == "BISHOP":
        is_valid = bishop_move(start_x, start_y, end_x, end_y)
    elif piece == "QUEEN":
        is_valid = queen_move(start_x, start_y, end_x, end_y)
    elif piece == "KNIGHT":
        is_valid = knight_move(start_x, start_y, end_x, end_y)

    return is_valid

# binary -> 2^n, n = bits
# 5 -> binary
# 5/2 = 2, % = 1
# 2/2 = 1, % = 0
# 1/2 = 0, % = 1
# 101 -> 2^0 + 2^1 + 2^2