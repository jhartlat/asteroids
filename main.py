import pygame
from constants import *
from player import Player


def main():
    # Initialize pygame
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Set up game clock
    clock = pygame.time.Clock()
    dt = 0

    # Set up the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set the containers for the Player class
    Player.containers = (updatable, drawable)

    # Instantiate a player object
    x_pos = SCREEN_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2
    player = Player(x=x_pos, y=y_pos)

    # Set up the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        pygame.Surface.fill(screen, 'black')

        # Iterate over all updatable objects
        for sprite in updatable:
            sprite.update(dt)

        # Iterate over all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        # Update the display
        pygame.display.flip()

        # Convert delta_time from miliseconds to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
