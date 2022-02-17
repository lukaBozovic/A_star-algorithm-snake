import copy
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, problem):
        
        actions = problem.actions(self.state)
        child_nodes = []
        for action in actions:
            successor_state = problem.result(self.state, action)
            child_nodes.append(Node(successor_state, self, action, self.path_cost+problem.get_cost(self.state, successor_state, action)))
           
        return child_nodes

    def path(self):

        path = [self.action]
        node = self.parent
        
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
            

        return path[::-1]

    def __lt__(self, node):

        return self.path_cost < node.path_cost
