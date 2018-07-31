

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[-1 for x in range(width+1)] for y in range(height+1)]

    def countPaths(self, pathsDown, pathsRight):
        count = 0
        if self.grid[pathsRight][pathsDown] != -1:
            count = self.grid[pathsRight][pathsDown]
        else:
            if pathsDown == 0 or pathsRight == 0:
               count = 1
            else:
                count = self.countPaths(pathsDown-1, pathsRight) + self.countPaths(pathsDown, pathsRight-1)
            self.grid[pathsRight][pathsDown] = count
        return count

n = 300
g = Grid(n, n)
print(g.countPaths(n,n))

#paths = []
#for n in range(2, 15):
#    paths.append(countPaths(n, n))

#print(paths)
#for i in range(len(paths)-1):
#    print(paths[i+1]/paths[i])