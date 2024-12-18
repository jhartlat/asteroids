# Asteroids Game

A modern Python remake of the classic **Asteroids** arcade game, built using the **Pygame** library. This project incorporates Object-Oriented Programming (OOP) principles to provide a structured and extensible gameplay experience.

## Features

- **Player-Controlled Spaceship**:
  - Rotate, move, and shoot bullets using keyboard controls.
  - Cooldown system for shooting to balance gameplay.

- **Dynamic Asteroids**:
  - Randomly spawned asteroids with varying sizes and velocities.
  - Splitting mechanic: Large asteroids split into smaller ones upon being hit.

- **Bullet Mechanics**:
  - Bullets destroy asteroids on collision.
  - Controlled by a cooldown system.

- **Collision Detection**:
  - Player collision with asteroids ends the game.
  - Bullets and asteroid collisions trigger the splitting mechanic.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd asteroids
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3.  Run the game:
    ```bash
    python main.py
## Controls
- W: Move forward
- S: Move backward
- A: Rotate counter-clockwise
- D: Rotate clockwise
- SPACE: Shoot bullets

## Requirements
- Python 3.7+
- Pygame 2.6.1 (specified in `requirements.txt`)


## Game Design
The game operates at a fixed 60 FPS and uses `pygame.sprite.Group` to manage updatable and drawable objects efficiently. Object behavior is defined in dedicated classes, making it easy to extend functionality.

## Future Improvements
- Add a scoring system
- Introduce power-ups or special weapons
