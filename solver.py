from board import GRID_SIZE
from visualization import draw_grid

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(GRID_SIZE)]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board, original_board, screen):
    empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if board[row][col] == 0]
    catch = {}

    # Determine valid numbers for each empty cell
    for row in range(len(board)):
        for col in range(len(board[row])):
            catch[(row, col)] = []
            if board[row][col] == 0:
                unvalid_number = []
                for num in range(1, 10):
                    if not is_valid(board, num, (row, col)):
                        unvalid_number.append(num)
                catch[(row, col)] = [n for n in range(1, 10) if n not in unvalid_number]

    while True:
        had_changed = False
        for (row, col) in catch:
            if len(catch[(row, col)]) == 1:
                num = catch[(row, col)][0]
                for i in range(9):
                    if len(catch[(row, i)]) != 0 and num in catch[(row, i)] and i != col:
                        catch[(row, i)].remove(num)
                        had_changed = True
                    if len(catch[(i, col)]) != 0 and num in catch[(i, col)] and i != row:
                        catch[(i, col)].remove(num)
                        had_changed = True
        if not had_changed:
            break

    # Backtracking function
    def backtrack(index):
        if index == len(empty_cells):
            return True

        row, col = empty_cells[index]
        for num in catch[(row, col)]:
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                draw_grid(screen, board, original_board, highlight_pos=(row, col))

                if backtrack(index + 1):
                    return True

                board[row][col] = 0
                draw_grid(screen, board, original_board, highlight_pos=(row, col))

        return False

    return backtrack(0)