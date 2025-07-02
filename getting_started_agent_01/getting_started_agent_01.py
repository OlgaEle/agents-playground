# 🔍 Just an agent that is moving around without reason — it randomly picks a direction and takes one step on the grid

# Import libraries
import numpy as np
import random

# Create a 10x10 grid filled with zeros (think of it like a map or game board)
world = np.zeros((10, 10), dtype=int)

# Pick a random starting position on the grid
i = random.randint(0, 9)  # Row index
j = random.randint(0, 9)  # Column index

# Place a "1" at the starting position to show where our character (agent) is
world[i][j] = 1

# Print the grid with the starting position marked
print(world)

# Reset the current position back to 0
world[i][j] = 0

# Choose a random direction to move: up, down, right, or left
move = random.choice(['up', 'down', 'right', 'left'])

# Apply the move, but only if it's within the boundaries of the grid
if move == 'up' and i > 0:
    i -= 1  # Move one step up (decrease row index)
elif move == "down" and i < 9:
    i += 1 # Move one step down (increase row index)
elif move == "right" and j < 9:
    j += 1
elif move == 'left' and j > 0:
    j -= 1

# Mark the new position with a "1"
world[i][j] = 1

# Print the final grid in a cleaner way (each row on a new line, no commas)
for row in world:
    print("".join(str(cell) for cell in row))

# 🤖 ❤️
