import pygame
import sys
import matplotlib.pyplot as plt
import random
import datetime

DEFAULT_MAX_CAP = 5

DIMENSIONS = (1000, 800)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.y and self.y == other.y


class QuadTree:
    def __init__(self, max_cap = DEFAULT_MAX_CAP, x = 0, y = 0, dim = DIMENSIONS):
        self.is_divided = False
        self.max_cap = max_cap
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None
        self.points = []
        self.num_points = 0
        
        # (0, 0) is the top-left corner of the window

        self.x = x    
        self.y = y
        self.dim = dim   # dim is a tuple (width, height)
    
    def point_is_within_bounds(self, point):
        return point.x >= self.x and point.x <= self.x + self.dim[0] and point.y >= self.y and point.y <= self.y + self.dim[1]
    
    def divide(self):
        if self.is_divided:
            return
        
        self.top_left = QuadTree(self.max_cap, self.x, self.y, (self.dim[0]/2, self.dim[1]/2))
        self.top_right = QuadTree(self.max_cap, self.x + self.dim[0]/2, self.y, (self.dim[0]/2, self.dim[1]/2))
        self.bottom_left = QuadTree(self.max_cap, self.x, self.y + self.dim[1]/2, (self.dim[0]/2, self.dim[1]/2))
        self.bottom_right = QuadTree(self.max_cap, self.x + self.dim[0]/2, self.y + self.dim[1]/2, (self.dim[0]/2, self.dim[1]/2))
        self.is_divided = True

    
    def insert_point(self, point):
        if not self.point_is_within_bounds(point):
            return
        
        if self.num_points < self.max_cap:
            self.points.append(point)
            self.num_points += 1
            return
        
        if not self.is_divided:
            self.divide()
        
        self.top_left.insert_point(point)
        self.top_right.insert_point(point)
        self.bottom_left.insert_point(point)
        self.bottom_right.insert_point(point)

    
    def contains_point(self, point):
        if not self.point_is_within_bounds(point):
            return False

        for p in self.points:
            if p.x == point.x and p.y == point.y:
                return True

        if not self.is_divided:
            return False
        else:
            return self.top_left.contains_point(point) or self.top_right.contains_point(point) or self.bottom_left.contains_point(point) or self.bottom_right.contains_point(point)
        
    
    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(point.x, point.y, 5, 5))
        
        if self.is_divided:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x + self.dim[0]/2, self.y, 2, self.dim[1]))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y + self.dim[1]/2, self.dim[0], 2))
            self.top_left.draw(screen)
            self.top_right.draw(screen)
            self.bottom_left.draw(screen)
            self.bottom_right.draw(screen)




def visualize():
    
    # Setup PyGame
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONS)
    

    # Setup Quadtree

    quadtree = QuadTree()

    running = True
    mouse_down = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP and mouse_down:
                pos = pygame.mouse.get_pos()
                quadtree.insert_point(Point(pos[0], pos[1]))
                mouse_down = False
    
        quadtree.draw(screen)
        pygame.display.flip()



def plot_speedup():

    
    X = []  # Number of points 
    l_search = []  #Time for Linear Search
    q_search = [] # Time for QuadTree search
    y = [] # Speed up

    MIN_NUM_POINTS = 1000
    MAX_NUM_POINTS = 2000

    for i in range(MIN_NUM_POINTS, MAX_NUM_POINTS + 1):

        
        X.append(i)

        quadtree = QuadTree()
        points = []

        for _ in range(1, i+1):

            point = Point(random.randrange(0, DIMENSIONS[0]), random.randrange(0, DIMENSIONS[1]))
            points.append(point)
            quadtree.insert_point(point)
    
            
        # Select middle point to find    
        point_to_find = points[len(points)//2]

        # Linear Search
        start = datetime.datetime.now()
        for point in points:
            if point.x == point_to_find.x and point.y == point_to_find.y:
                end = datetime.datetime.now()
                l_search.append((end - start).microseconds)
                break
        

        # QuadTree search

        start = datetime.datetime.now()
        if quadtree.contains_point(point_to_find):
            end = datetime.datetime.now()
            q_search.append((end - start).microseconds)
        

    y = []
    for i in range(1, len(l_search)):
        y.append(float(l_search[i]/q_search[i]))

    plt.plot(X ,y)
    plt.show()    

            
                

                


    




def main():

    num_args = len(sys.argv) - 1

    if num_args == 1 and (sys.argv[1].lower() == "--visualize"  or "-v"):
        visualize()
    else:
        plot_speedup()



if __name__ == "__main__":
    main()


