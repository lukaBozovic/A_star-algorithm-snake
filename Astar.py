from copy import deepcopy
from Node import Node
from Snake import Snake
from queue import Queue, PriorityQueue
import math
import random
import pygame 



def a_star(problem):
    
    frontier = PriorityQueue()
    frontier.put(Node(problem.initial))
    br = 0
    explored = []

    while not frontier.empty():

        node = frontier.get()
        explored.append(node.state)

        if problem.goal_test(node.state):
            return node.path(), br
            

        for child_node in node.expand(problem):
            br+=1
            if not child_node.state in explored:
                frontier.put(child_node)
    
    return None, br
 
def inverse_action(action):
        if action == "DOWN":
            return "UP"

        if action == "UP":
            return "DOWN"

        if action == "LEFT":
            return "RIGHT"
            
        if action == "RIGHT":
            return "LEFT"       

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

distances = [[0, 1, 2, 3],
             [1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 6]]
problem = Snake([[3, 3], [2, 3]], [0,0], 4, distances)


def print_table(state, goal, dimension):
    
    for i in range(dimension):
        for j in range(dimension):
            if [i, j] in state:
                print(" o ", end = " ")
            elif [i, j] == goal:
                print(" x ", end = " ")
            else:
                print(" - ", end = " ")    
        print()
    print()

def make_distances(dimension, goal):
    distances = []

    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(heuristic([i, j], goal))
        distances.append(row)  

    return distances      

def generate_new_goal(state, dimension):
    avaliable_values = []
    for i in range(dimension):
        for j in range(dimension):
            if [i, j] not in state:
                avaliable_values.append([i,j])

    return random.choice(avaliable_values)          

def draw_circles(win, dimension, state, goal):
    win.fill((255, 255, 255))

    field_len = 500 // dimension
    colour = (20,80,0)
    colour1 = (0,0,0)
    
    pygame.draw.circle(win, colour1, (goal[0]*field_len+field_len//2, goal[1]*field_len+field_len//2), field_len//2, 0)
    for i in state:
        pygame.draw.circle(win, colour, (i[0]*field_len+field_len//2, i[1]*field_len+field_len//2), field_len//2, 0)

def play(dimension):
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    win.fill((255, 255, 255))
    br = 0
    distances = make_distances(dimension, [dimension-1, dimension-1])
    res = 0
    goal =  [dimension-1, dimension-1]    
    problem = Snake([[0, 1], [0, 0]], goal, dimension, distances)
    while True:
        node_path, temp_br = a_star(problem)
        br+=temp_br
        if node_path == None:
            print("Kraj igre", res)
            pygame.quit()
            break
        
        res+=1
        old_state_parent = None
        old_state = problem.initial
        
        draw_circles(win, dimension, old_state, problem.goal)
        clock = pygame.time.Clock()
        clock.tick(10)
        
        pygame.display.update()
        for i in node_path:
            new_state = problem.result(old_state, i)
            draw_circles(win, dimension, new_state, problem.goal)
            pygame.display.update()
        
            clock.tick(10)
            old_state_parent = deepcopy(old_state)
            old_state = deepcopy(new_state)

        old_state_parent.insert(0, goal)
        goal = generate_new_goal(old_state_parent, dimension)
        distances = make_distances(dimension, goal)
        problem = Snake(old_state_parent, goal, dimension, distances)
    
    #print(res)  
    #print(br) 
    pygame.quit()
    return br

#br = 0
#for i in range(10):         
#   br += play(7)
#print(br/10)   
print(play(8))
#print(a_star(problem))
 

