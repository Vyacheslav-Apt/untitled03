import random
import time
dx = 2  #координата игрока по x во время спавна
dy = 9  #координата игрока по y
dp = 0

siniy = "blue"   #цвета кубиков
sheltyy = "yellow"
rozoviy = "pink"

maze = []


time.sleep(5)
for i in range(1):
    if random.randint(0, 4) == 0:
        maze.append(0)
        maze.append(0)
    elif random.randint(0, 4) == 1:
        maze.append(1)
        maze.append(0)
    elif random.randint(0, 4) == 2:
        maze.append(2)
        maze.append(0)
    elif random.randint(0, 4) == 3:
        maze.append(3)
        maze.append(0)
    else:
        maze.append(4)
        maze.append(0)
    if random.randint(7,9) == 7:
        maze.append(sheltyy)
    elif random.randint(7,9) == 8:
        maze.append(rozoviy)
    else:
     maze.append(siniy)

print(maze)