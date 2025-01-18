import pygame
from constants import GRID_SIZE, CELL_SIZE, PADDING, WHITE, GRAY, DARK_GRAY, GREEN, BLACK, BLUE

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = GRID_SIZE * CELL_SIZE + 2 * PADDING
SCREEN_HEIGHT = GRID_SIZE * CELL_SIZE + 2 * PADDING
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Solver Visualization")


def draw_grid(screen, board, original_board, highlight_pos=None):
    screen.fill(WHITE)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = PADDING + col * CELL_SIZE
            y = PADDING + row * CELL_SIZE

            # Draw the cell rectangle with alternating colors
            pygame.draw.rect(screen, GRAY if (row + col) % 2 == 0 else DARK_GRAY, (x, y, CELL_SIZE, CELL_SIZE))

            # Highlight the current cell
            if highlight_pos == (row, col):
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

            # Draw the number if it exists
            if board[row][col] != 0:
                font = pygame.font.Font(pygame.font.get_default_font(), 36)
                color = BLACK if original_board[row][col] != 0 else BLUE
                text = font.render(str(board[row][col]), True, color)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)

    # Draw grid lines
    for i in range(GRID_SIZE + 1):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (PADDING, PADDING + i * CELL_SIZE), (SCREEN_WIDTH - PADDING, PADDING + i * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (PADDING + i * CELL_SIZE, PADDING), (PADDING + i * CELL_SIZE, SCREEN_HEIGHT - PADDING), line_width)

    pygame.display.flip()
