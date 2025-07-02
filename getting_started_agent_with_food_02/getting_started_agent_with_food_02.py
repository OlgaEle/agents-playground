# 🔍 Just an agent and some food on a grid —  
# the agent and the food are placed randomly, and that's it (I think our agent doesn't even know that the food exists 😅).

# Import libraries
import numpy as np
import random

# 📦 Define the size of our square grid world (10x10)
grid_size = 10

# 🗺️ Create the grid, filled with 0s (empty spaces)
world = np.zeros((grid_size, grid_size), dtype=int)

# 🤖 Randomly place the agent somewhere on the grid
agent_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
world[agent_position[0], agent_position[1]] = 1  # Mark the agent with a 1

# 🍝 Now let's place some food on the grid, but NOT on the agent
while True:
    food_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    if food_position != agent_position:
        break  # Found a spot that's not already taken by the agent

# 🍝 Place the food on the grid (marked as 2)
world[food_position[0], food_position[1]] = 2

# 🖨️ Show the final grid (agent = 1, food = 2, empty = 0)
world
