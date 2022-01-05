import numpy as np

n = int(input("Introduceti dimensiunea:"))

grid = [[0 for i in range(n)] for j in range(n)]


# print(grid)
# agent - 1, destinatie - 2, gheata - 3

def update_grid(grid, i, j, k):
    grid[i][j] = k


def reset_grid(grid):
    update_grid(grid, 0, 0, 1)
    update_grid(grid, 3, 3, 2)
    update_grid(grid, 1, 3, 3)
    update_grid(grid, 2, 3, 3)
    update_grid(grid, 1, 1, 3)
    update_grid(grid, 3, 0, 3)


q_table = np.random.random((16, 4))
learning_rate = 0.05
gama = 0.99
num_episodes = 10000
max_steps_per_episode = 100


def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return i, j


# sus = 0, jos = 1, stanga = 2, dreapta = 3
def move(direction):
    position = find(1, grid)
    done = False
    reward = 0
    if direction == 0:
        if position[0] - 1 > -1:
            if grid[position[0] - 1][position[1]] == 2:
                done = True
                reward = 1
            if grid[position[0] - 1][position[1]] == 3:
                done = True
                reward = -1
            update_grid(grid, position[0] - 1, position[1], 1)
            update_grid(grid, position[0], position[1], 0)
        else:
            reward = 0
    if direction == 1:
        if position[0] + 1 < n:
            if grid[position[0] + 1][position[1]] == 2:
                done = True
                reward = 1
            if grid[position[0] + 1][position[1]] == 3:
                done = True
                reward = -1
            update_grid(grid, position[0] + 1, position[1], 1)
            update_grid(grid, position[0], position[1], 0)
        else:
            reward = 0
    if direction == 2:
        if position[1] - 1 > -1:
            if grid[position[0]][position[1] - 1] == 2:
                done = True
                reward = 1
            if grid[position[0]][position[1] - 1] == 3:
                done = True
                reward = -1
            update_grid(grid, position[0], position[1] - 1, 1)
            update_grid(grid, position[0], position[1], 0)
        else:
            reward = 0
    if direction == 3:
        if position[1] + 1 < n:
            if grid[position[0]][position[1] + 1] == 2:
                done = True
                reward = 1
            if grid[position[0]][position[1] + 1] == 3:
                done = True
                reward = -1
            update_grid(grid, position[0], position[1] + 1, 1)
            update_grid(grid, position[0], position[1], 0)
        else:
            reward = 0
    position2 = find(1, grid)
    return position2, done, reward


reset_grid(grid)


def q_learning():
    global rewards_all_episodes
    count = 0
    for episode in range(num_episodes):
        done = False
        reset_grid(grid)
        rewards_current_episode = 0
        agent = find(1, grid)
        for step in range(max_steps_per_episode):
            # print(agent)
            temp = agent[0] * 4 + agent[1]
            maximum = np.max(q_table[temp])
            # print(q_table[temp])
            action = np.where(q_table[temp] == maximum)
            new_state, done, reward = move(action[0][0])
            #print(new_state)
            temp2 = new_state[0] * 4 + new_state[1]
            q_table[temp][action[0][0]] = q_table[temp][action[0][0]] * (1 - learning_rate) + \
                                          learning_rate * (reward + gama * max(q_table[temp2]))
            agent = new_state
            rewards_current_episode += reward
            if done:
                #count += 1
                break
print("TABELA Q INITIALA")
print(q_table)
q_learning()
print("TABELA Q DUPA INVATARE")
print(q_table)

