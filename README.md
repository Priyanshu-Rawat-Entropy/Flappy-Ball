# Flappy Ball

A simple 2D arcade game inspired by **Flappy Bird**, built from scratch using **Python and Pygame**.
Instead of a bird, the player controls a ball and tries to pass through randomly generated obstacles without hitting them.

## Game Overview

The game continuously updates the ball's movement, generates obstacles, checks for collisions, and keeps track of the player's score.

The main goal is to survive as long as possible and achieve a high score.

## Features

* Gravity-based ball movement
* Space, Up Arrow, and mouse controls
* Randomly generated obstacles
* Collision detection
* Score tracking
* High-score saving using a text file
* Game-over detection
* Restart functionality
* Dynamic colors and visual effects
* 90 FPS game loop

## Technologies Used

| Technology | Usage                                        |
| ---------- | -------------------------------------------- |
| Python     | Main programming language                    |
| Pygame     | Game window, graphics, input, and game loop  |
| Random     | Random obstacle positions and visual effects |
| File I/O   | Saving and loading the high score            |

## How It Works

### 1. Player Movement

The ball is affected by gravity, which continuously moves it downward.

Pressing **Space**, **Up Arrow**, or the **Left Mouse Button** changes its vertical movement and makes the ball move upward.

### 2. Obstacle Generation

Obstacles are created at regular time intervals.

Their height is randomly selected, creating a different arrangement during each game.

The obstacles move from right to left across the screen.

### 3. Collision Detection

The game checks whether the ball overlaps with an obstacle.

A collision also occurs if the ball moves outside the playable area.

When a collision occurs, the game enters the **Game Over** state.

### 4. Scoring

When an obstacle successfully passes the player, the score increases.

The highest score is stored in `score.txt` so it can be used in future games.

## Game Flow

```text
Start
  ↓
Initialize Pygame
  ↓
Load High Score
  ↓
Create Player
  ↓
Start Game Loop
  ↓
Read User Input
  ↓
Apply Gravity
  ↓
Generate & Move Obstacles
  ↓
Check Collision
  ↓
Update Score
  ↓
Render Game
  ↓
Game Over?
 ┌───────┴───────┐
No              Yes
 ↓                ↓
Continue       Show Game Over
Game Loop          ↓
                Restart / Exit
```

## Controls

| Input               | Action           |
| ------------------- | ---------------- |
| `Space`             | Move ball upward |
| `Up Arrow`          | Move ball upward |
| `Left Mouse Button` | Move ball upward |
| `Enter`             | Restart the game |
| Window Close        | Exit the game    |

## Installation

Install Pygame:

```bash
pip install pygame
```

Clone the repository:

```bash
git clone https://github.com/Priyanshu-Rawat-Entropy/Flappy-Ball.git
```

Run the game:

```bash
python main.py
```

> Make sure the `score.txt` file path in the code is correctly configured for your system.
