import copy
class Snake:

    def __init__(self, initial, goal, dimension, distances):
        self.initial = initial
        self.goal = goal
        self.dimension = dimension
        self.distances = distances

    def goal_test(self, state):

        return state[0] == self.goal

    def actions(self, state):
        possible_actions = ["UP", "DOWN", "LEFT", "RIGHT"]
        row = state[0][0]
        col =state[0][1]

        if row + 1 >= self.dimension:
            possible_actions.remove("DOWN")
        elif [row+1, col] in state:
            possible_actions.remove("DOWN")   

        if row - 1 < 0:
            possible_actions.remove("UP")
        elif [row - 1, col] in state:
            possible_actions.remove("UP")  

        if col + 1 >= self.dimension:
            possible_actions.remove("RIGHT")
        elif [row, col + 1] in state:
            possible_actions.remove("RIGHT")    

        if col - 1 < 0:
            possible_actions.remove("LEFT")  
        elif [row, col - 1] in state:
            possible_actions.remove("LEFT")          
        
        
        return possible_actions

    def result(self, state, action):
        new_state = copy.deepcopy(state)
        i = len(state)-1
        while i > 0:
            new_state[i] = copy.deepcopy(state[i-1])
            i -= 1
        
        
        if action == "UP":
            new_state[0][0] -= 1 
            return new_state
            
        if action == "DOWN":
            new_state[0][0] += 1 
            return new_state

        if action == "LEFT":
            new_state[0][1] -= 1 
            return new_state

        if action == "RIGHT":
            new_state[0][1] += 1 
            return new_state

    def get_cost(self, parentState, state, action):
        #return 1
        return 1 + self.distances[state[0][0]][state[0][1]]