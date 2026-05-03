# search.py
# Carlos Salas Alarcón
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
    from util import Stack
    
    # Inicializamos Set de Visitados
    visited = set()

    
    # Creamos la Cola de Exploración
    frontier = util.Stack()
    # Añadimos a la cola el Origen
    frontier.push((problem.getStartState(), []))
    
    # Mientras haya Cola de Exploración
    while not frontier.isEmpty():
        # Sacamos para usar una casilla de la Cola de Exploración
        state, actions = frontier.pop() # Porque no pide cost?

        # Si es el objetivo
        if problem.isGoalState(state):
            return actions

        # Añadimos a Visitados
        if state not in visited:
            visited.add(state)
        
            # Por cada Sucesor
            for next_state, action, _ in problem.getSuccessors(state):
                # Si no está visitado
                if next_state not in visited:
                    # Añadimos a la cola de Exploración
                    # y Stackeamos las Acciones hasta llegar ahí
                    frontier.push((next_state, actions + [action]))


    # En caso de error -> Lista Vacia
    return []
    
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""    
    from util import Queue
        
    # Inicializamos Set de Visitados
    visited = set()
    
    # Creamos la Cola de Exploración
    frontier = util.Queue()
    # Añadimos a la cola el Origen
    frontier.push((problem.getStartState(), []))
    
    # Mientras haya Cola de Exploración
    while not frontier.isEmpty():
        # Sacamos para usar una casilla de la Cola de Exploración
        state, actions = frontier.pop() # Porque no pide cost?

        # Si es el objetivo
        if problem.isGoalState(state):
            return actions

        # Añadimos a Visitados
        if state not in visited:
            visited.add(state)
        
            # Por cada Sucesor
            for next_state, action, _ in problem.getSuccessors(state):
                # Si no está visitado
                if next_state not in visited:
                    # Añadimos a la cola de Exploración
                    # y Stackeamos las Acciones hasta llegar ahí
                    frontier.push((next_state, actions + [action]))
            
    # En caso de error -> Lista Vacia
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    from util import PriorityQueue
    
    # Inicializamos Set de Visitados
    visited = set()
    
    # Creamos la Cola de Prioridad
    frontier = PriorityQueue()
    
    #  En UCS guardamos (estado, acciones, coste_acumulado)
    # PriorityQueue.push() pide el elemento y el coste
    frontier.push((problem.getStartState(), [], 0), 0)
    
    while not frontier.isEmpty():
        # Ahora el pop nos devuelve 3 elementos
        state, actions, cost = frontier.pop()

        if problem.isGoalState(state):
            return actions

        # Se añade a visitado después del POp
        if state not in visited:
            visited.add(state)
        
            for next_state, action, step_cost in problem.getSuccessors(state):
                if next_state not in visited:
                    # Calculamos el nuevo coste total para llegar a este vecino
                    new_cost = cost + step_cost
                    # Lo añadimos a la frontera con su nueva prioridad
                    frontier.push((next_state, actions + [action], new_cost), new_cost)
            
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    
    frontier = PriorityQueue()
    # Usamos un diccionario para registrar el coste al que llegamos a cada estado
    visited = {} 
    
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)
    
    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()
        
        # No lo exploramos si ya hemos llegado a el por un camino más barato
        if state in visited and visited[state] <= cost:
            continue
            
        visited[state] = cost
        
        if problem.isGoalState(state):
            return actions
            
        for next_state, action, step_cost in problem.getSuccessors(state):
            # Añadimos la heurística al coste
            f = cost + step_cost + heuristic(next_state, problem)
            frontier.push(
                (next_state, actions + [action], cost + step_cost),
                f
            )
            
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
