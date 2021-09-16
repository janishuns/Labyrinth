import numpy as np
import matplotlib.pyplot as plt

# Creates a maze of specified height and width
n = 50  # height
m = 80  # width
spikyless = 1 # you can try to make it slightly slightly harder by increasing this

# x and y give the points to be plotted
x = [0, int(round(n / 2)), round(n / 2) + 1, n, 0, round(n / 2) - 1, round(n / 2), n, 0, 0, n, n]
y = [0, 0, 0, 0, m, m, m, m, 0, m, 0, m]
line_list = []  # list of the lines added

# write down the side points
point_list = [] # point_list holds all the points that end walls
for i in range(n):
    point_list.append([i, 0]),point_list.append([i, -1])
    point_list.append([i, m]),point_list.append([i, m+1])
for i in range(m):
    point_list.append([0, i]),point_list.append([-1, i])
    point_list.append([n, i]),point_list.append([n+1, i])

available_points = [] # available_points holds all the points from which new walls may be drawn
for i in range(n - 2):
    available_points.append([i + 1, 0])
    available_points.append([i + 1, m])
for i in range(m - 2):
    available_points.append([0, i + 1])
    available_points.append([n, i + 1])

def check_if_in(item, list):  # True if item is in the list
    for i in list:
        if i == item:
            return True
    return False

def new_line():  # creates a new line that doesn't close anything off, unless it fails 10 times in a row
    [x1, y1] = available_points[np.random.choice(range(len(available_points)))]  # choose point from pointlist

    # choose direction
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ch = np.random.choice(range(4))
    [x2, y2] = [x1 + dir[ch][0], y1 + dir[ch][1]]

    # check if the line is valid
    if check_if_in([x2, y2], point_list):
        # check if the point is valid
        surr = 0
        for i in dir:
            if check_if_in([x1+i[0],y1+i[1]],point_list):
                surr+=1 # count the surrounding unavailable points
        if check_if_in([x1,y1],available_points) and surr==4:
            for i in range(spikyless):
                available_points.remove([x1,y1])
        return
    else:  # add the line and point to the lists if valid
        point_list.append([x2, y2])
        for i in range(spikyless): # to grow the larger trees even larger
            available_points.append([x2,y2])
        line_list.append([x1, x2, y1, y2])
        x.append(x1), x.append(x2)
        y.append(y1), y.append(y2)

while len(available_points)>0:
    [x1, y1] = available_points[np.random.choice(range(len(available_points)))] # choose point from pointlist
    new_line()

# you'd like to see it wouldn't you...
def draw(x, y):
    for i in range(0, len(x), 2):
        plt.plot(x[i:i + 2], y[i:i + 2], 'b')
    plt.show()
draw(x, y)