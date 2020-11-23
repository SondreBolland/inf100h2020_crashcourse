'''
 X | X | O
----------
   | O |
----------
 X |   |
'''
def place_tile(board, tile, x, y):
    height = len(board)
    width = len(board[0])
    if x < 0 or x > width:
        raise ValueError("x coordinate is too high/low")
    if y < 0 or y > height:
        raise ValueError("y coordinate is too high/low")
    '''
    write the rest here...
    '''