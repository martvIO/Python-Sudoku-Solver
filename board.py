from constants import GRID_SIZE

def string_to_board(sudoku_string):
    return [[int(sudoku_string[row * GRID_SIZE + col]) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
