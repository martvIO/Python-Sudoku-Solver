import pygame
import time
from constants import GRID_SIZE, PADDING, WHITE
from board import string_to_board
from visualization import draw_grid, screen
from solver import solve_sudoku

def main():
    # Initial Sudoku board setup
    sudoku_string = "070000300040053900900008000006000004300049000005000060000100200050000700000070051"
    board = string_to_board(sudoku_string)
    original_board = [row[:] for row in board]

    running = True
    draw_grid(screen, board, original_board)
    time.sleep(1)

    solve_thread_started = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if not solve_thread_started:
            solve_sudoku(board, original_board, screen)
            solve_thread_started = True

        pygame.time.Clock().tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
