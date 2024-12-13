import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Remove the current asteriod
        self.kill()

        # If the asteroid is small, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate the radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate random angles for the new velocities
        random_angle = random.uniform(20, 50)

        # Create new velocity vectors
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2

        # Add them to the appropriate groups
        for container in self.containers:
            container.add(asteroid1, asteroid2)
            
