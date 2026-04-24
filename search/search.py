# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    
    # Inicializamos Set de Visitados
    visited = set()
    # Conseguimos Origen
    startState = problem.getStartState()
    # Añadimos Origen a Visitados
    visited.add(startState)

    # Initialise the frontier with the start state and an empty action list
    # Declaramos la Frontera
    # STACK -> LIFO (DFS)
    # Ejemplo .getSuccesors() -> ((5, 4), 'South', 1)
    
    # Creamos la Cola de Exploración
    frontier = util.Stack()
    # Añadimos a la cola el Origen
    frontier.push((startState, [], 1))
    
    # Mientras haya Cola de Exploración
    while not frontier.isEmpty():
        # Sacamos para usar una casilla de la Cola de Exploración
        state, actions = frontier.pop() # Porque no pide cost?
        # Conseguimos sus sucesores
        successors = problem.getSuccessors(state)
        # Por cada Sucesor
        for next_state, action, _ in successors:
            # Si no está visitado
            if next_state not in visited:
                # Añadimos a la cola de Exploración
                # y Stackeamos las Acciones hasta llegar ahí
                frontier.push((next_state, actions + [action]))
            # Si es el objetivo
            if problem.isGoalState(state):
                # Ganamos
                return actions
            # Sino es, repetimos el bucle
    # En caso de error -> Lista Vacia
    return []
    
    '''#def dfs_numpy(graph, source, target):
    nodes = list(graph.nodes()) 
    adjacency_matrix = nx.to_numpy_array(graph, nodelist=nodes)

    visited = np.zeros(len(nodes), dtype=bool)
    source_index = nodes.index(source)
    target_index = nodes.index(target)
    visited[source_index] = True

    to_explore = [source_index]
    current_position = len(to_explore) - 1  # DFS: always the last element

    parent = np.ones(len(nodes), dtype=int) * -1
    steps = 0

    while len(to_explore) > 0:
        steps += 1
        current_index = to_explore[current_position]
        to_explore.pop(current_position)

        if current_index == target_index:
            break

        neighbors = np.where(adjacency_matrix[current_index] == 1)[0]
        for neighbor_index in neighbors:
            if not visited[neighbor_index]:
                visited[neighbor_index] = True
                to_explore.append(neighbor_index)
                current_position = len(to_explore) - 1
                parent[neighbor_index] = current_index

        if len(to_explore) > 0:
            current_position = len(to_explore) - 1

    path = []
    if parent[target_index] != -1 or source_index == target_index:
        current = target_index
        while current != -1:
            path.insert(0, nodes[current])
            current = parent[current]

    return steps, path'''
    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    
    # BFS -> FIFO -> util.queue
        # Inicializamos Set de Visitados
    visited = set()
    # Conseguimos Origen
    startState = problem.getStartState()
    # Añadimos Origen a Visitados
    visited.add(startState)

    # Initialise the frontier with the start state and an empty action list
    # Declaramos la Frontera
    # STACK -> LIFO (DFS)
    # Ejemplo .getSuccesors() -> ((5, 4), 'South', 1)
    
    # Creamos la Cola de Exploración
    frontier = util.Queue()
    # Añadimos a la cola el Origen
    frontier.push((startState, []))
    
    # Mientras haya Cola de Exploración
    while not frontier.isEmpty():
        # Sacamos para usar una casilla de la Cola de Exploración
        state, actions = frontier.pop() # porque no pide costs?
        # Si es el objetivo
        if problem.isGoalState(state):
            # Ganamos
            return actions
        # Conseguimos sus sucesores
        successors = problem.getSuccessors(state)
        # Por cada Sucesor
        for next_state, action, _ in successors:
            # Si no está visitado
            if next_state not in visited:
                # Añadimos a la Lista de Visitados
                visited.add(state)
                # Añadimos a la cola de Exploración
                # y Stackeamos las Acciones hasta llegar ahí
                frontier.push((next_state, actions + [action]))
            
    # En caso de error -> Lista Vacia
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
