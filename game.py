import pygame
import random

# Window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Game board dimensions
BOARD_SIZE = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class Game:
    def __init__(self):
        self.board = self.initialize_board()
        self.selected_tile = None
        self.game_over = False

    def initialize_board(self):
        # Initialize the game board with numbers 1-8 and an empty slot
        board = []
        for i in range(1, BOARD_SIZE * BOARD_SIZE):
            board.append(i)
        board.append(0)
        return board

    def shuffle_board(self):
        # Shuffle the game board
        random.shuffle(self.board)
        # Ensure the game is solvable
        while not self.is_solvable():
            random.shuffle(self.board)

    def is_solvable(self):
        # Check if the game is solvable
        inversions = 0
        for i in range(len(self.board)):
            for j in range(i + 1, len(self.board)):
                if self.board[i] > self.board[j] and self.board[i] != 0 and self.board[j] != 0:
                    inversions += 1
        return inversions % 2 == 0

    def move_tile(self, pos):
        # Move the selected tile to the clicked position
        if self.selected_tile is not None:
            selected_index = self.board.index(self.selected_tile)
            clicked_index = pos[0] + pos[1] * BOARD_SIZE
            if abs(selected_index - clicked_index) in [1, BOARD_SIZE]:
                self.board[selected_index], self.board[clicked_index] = self.board[clicked_index], self.board[selected_index]
                self.selected_tile = None
                self.check_game_over()

    def check_game_over(self):
        # Check if the game is over
        if self.board == self.initialize_board():
            self.game_over = True

def draw_board(screen, game):
    # Draw the game board
    screen.fill(WHITE)
    font = pygame.font.Font(None, 100)
    for i in range(len(game.board)):
        if game.board[i] != 0:
            text = font.render(str(game.board[i]), True, BLACK)
            screen.blit(text, (i % BOARD_SIZE * WINDOW_WIDTH // BOARD_SIZE + WINDOW_WIDTH // (2 * BOARD_SIZE) - text.get_width() // 2,
                               i // BOARD_SIZE * WINDOW_HEIGHT // BOARD_SIZE + WINDOW_HEIGHT // (2 * BOARD_SIZE) - text.get_height() // 2))
        if game.selected_tile is not None and game.board[i] == game.selected_tile:
            pygame.draw.rect(screen, YELLOW, (i % BOARD_SIZE * WINDOW_WIDTH // BOARD_SIZE, i // BOARD_SIZE * WINDOW_HEIGHT // BOARD_SIZE,
                                              WINDOW_WIDTH // BOARD_SIZE, WINDOW_HEIGHT // BOARD_SIZE), 5)
    pygame.display.update()

def main():
    # pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    shuffled = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = (pos[0] // (WINDOW_WIDTH // BOARD_SIZE), pos[1] // (WINDOW_HEIGHT // BOARD_SIZE))
                if game.selected_tile is None:
                    if game.board[pos[0] + pos[1] * BOARD_SIZE] != 0:
                        game.selected_tile = game.board[pos[0] + pos[1] * BOARD_SIZE]
                else:
                    game.move_tile(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not shuffled:
                    game.shuffle_board()
                    shuffled = True

        draw_board(screen, game)
        if game.game_over:
            print("Congratulations, you won!")
            running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
