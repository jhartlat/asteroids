import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes will override
        pass

    def update(self, dt):
        # Sub-classes will override
        pass

    def hasCollided(self, other):
        # Calculate the distance between this shape and the other shape
        distance = self.position.distance_to(other.position)

        # Check if the distance is less than or equal to the sum of the radii
        return distance <= (self.radius + other.radius)
