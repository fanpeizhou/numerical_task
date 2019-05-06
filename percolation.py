import numpy as np 
import matplotlib.pyplot as plt 
import copy

def generate_cell(size, p):
    cell = np.random.random((size,size))
    for i in range(size):
        for j in range(size):
            if cell[i, j] < p:
                cell[i, j] = 1   # can pass
            else:
                cell[i, j] = 0   # can't pass
    return cell        

def find_way_left(cell, way):
    for i in range(size):
        for j in range(size):
            if way[i, j] == 1:
                if i != 0:
                    if cell[i-1, j] == 1:    # up
                        way[i-1, j] = 1
                if i != size-1:
                    if cell[i+1, j] == 1:    # down
                        way[i+1, j] = 1
                if j != 0:
                    if cell[i, j-1] == 1:    # left
                        way[i, j-1] = 1
                if j != size-1:
                    if cell[i, j+1] == 1:    # right
                        way[i, j+1] = 1
    return way

def find_way_right(cell, way):
    for i in range(size):
        for j in reversed(range(size)):
            if way[i, j] == 1:
                if i != 0:
                    if cell[i-1, j] == 1:    # up
                        way[i-1, j] = 1
                if i != size-1:
                    if cell[i+1, j] == 1:    # down
                        way[i+1, j] = 1
                if j != 0:
                    if cell[i, j-1] == 1:    # left
                        way[i, j-1] = 1
                if j != size-1:
                    if cell[i, j+1] == 1:    # right
                        way[i, j+1] = 1
    return way

def main1():
    cell = generate_cell(size, p)
    way = np.zeros((size, size))
    way[0] = cell[0]
    n = 0
    while 1:
        n += 1
        print(n)
        mid = copy.deepcopy(way)
        way = find_way_right(cell, find_way_left(cell, way))
        if way[size-1].sum() >= 1:
            # n += 1
            print("pass")
            break
        mark = 0
        for i in range(size):
            for j in range(size): 
                if way[i][j] != mid[i][j]:
                    mark = 1
        if mark == 0:
            print("oh no pass")
            break
    plt.matshow(cell)           
    plt.matshow(way)
    plt.show()
    # return n

size = 20
p = 0.6

main1()
# times = 50
# # main()
# def main(times):
#     # n = 0
#     for i in range(times):
#         n = main1(n)
# #     # pep = n/times
# #     # print("percolation's p is %f " %pep)

# main(times)

