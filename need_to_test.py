import numpy as np
import matplotlib.pyplot as plt


# x, y = np.random.random(size=(2,10))

def draw(x, y):
    for i in range(0, len(x), 2):
        plt.plot(x[i:i + 2], y[i:i + 2], 'b')
    plt.show()


n = 50  # height
m = 80  # width

x = [0, int(round(n / 2)), round(n / 2) + 1, n, 0, round(n / 2) - 1, round(n / 2), n, 0, 0, n, n]
y = [0, 0, 0, 0, m, m, m, m, 0, m, 0, m]

line_list = []  # list of the lines added

# write down the side points
point_list = []
for i in range(n - 2):
    point_list.append([i + 1, 0])
    point_list.append([i + 1, m])
for i in range(m - 2):
    point_list.append([0, i + 1])
    point_list.append([n, i + 1])

available_points = []
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


def point_is_out(point):
    if point[0] > n - 1 or point[0] < 1 or point[1] > m - 1 or point[1] < 1:
        return True
    else:
        return False


def new_line(count):  # creates a new line that doesn't close anything off, unless it fails 100 times in a row
    [x1, y1] = available_points[np.random.choice(range(len(available_points)))]  # choose point from pointlist

    # choose direction
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ch = np.random.choice(range(4))
    [x2, y2] = [x1 + dir[ch][0], y1 + dir[ch][1]]

    # check if the line is valid
    if check_if_in([x2, y2], point_list) and count <= 100 or 1 > y2 or x2 < 1 or y2 > m - 1 or x2 > n - 1:
        # check if the surrounding points are in the point list
        surr = 0
        for i in dir:
            if check_if_in([x1+i[0],y1+i[1]],point_list):
                surr+=1
        if check_if_in([x1,y1],available_points) and surr==4:
            available_points.remove([x1,y1])
        new_line(count + 1)
    elif count > 100:
        return
    else:  # add it to the lists if it is valid
        point_list.append([x2, y2])
        available_points.append([x2,y2])
        line_list.append([x1, x2, y1, y2])
        x.append(x1), x.append(x2)
        y.append(y1), y.append(y2)

g=0
for i in range(n * m):
    try:
        [x1, y1] = available_points[np.random.choice(range(len(available_points)))]  # available_points[np.random.choice(range(len(available_points)))] # choose point from pointlist
    except:
        break
    # dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    g+=1
    print(g)
    new_line(0)


print(len(line_list))

draw(x, y)

### 2nd method for making new lines. This one produces tree-like labirinths ###
'''
def new_line(count):  # creates a new line that doesn't close anything off, unless it fails 100 times in a row
    [x1, y1] = point_list[np.random.choice(range(len(point_list)))] #choose point from pointlist

    #choose direction
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ch = np.random.choice(range(4)) 
    [x2,y2] = [x1+dir[ch][0],y1+dir[ch][1]]

    #check if the line is valid
    if check_if_in([x2, y2], point_list) and count <= 100 or 1>y2 or x2<1 or y2>m-1 or x2>n-1:
        new_line(count + 1)
    elif count>100:
        return
    else: #add it to the lists if it is
        point_list.append([x2, y2])
        line_list.append([x1, x2, y1, y2])
        x.append(x1), x.append(x2)
        y.append(y1), y.append(y2)
'''

### 1st method for making new lines. Not a labirinth ###
'''
def new_line():  # generate a new unit line
    new_x1 = np.random.choice(range(n - 2)) + 1
    new_y1 = np.random.choice(range(m - 2)) + 1
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ch = np.random.choice(range(4))  # choose direction
    new_x2 = new_x1 + dir[ch][0]
    new_y2 = new_y1 + dir[ch][1]
    return [new_x1, new_x2, new_y1, new_y2]
'''