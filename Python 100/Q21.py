# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:

from math import sqrt

def euclidean_distance_rounded(x, y):
    return round(sqrt(x**2 + y**2))

inputs = []
point = [0, 0]

while True:
    direction = input('[Direction] [Step]: ')
    if len(direction.split(' ')) == 2:
        inputs.append(direction)
    else:
        break

for move in inputs:
    direction, movement = move.split(' ')
    movement = int(movement)
    if direction.upper() == 'UP':
        point[1] += movement
    elif direction.upper() == 'DOWN':
        point[1] -= movement
    elif direction.upper() == 'RIGHT':
        point[0] += movement
    elif direction.upper() == 'LEFT':
        point[0] -= movement

print(euclidean_distance_rounded(point[0], point[1]))