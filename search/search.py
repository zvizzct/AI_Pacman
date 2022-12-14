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
import time


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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
        Search the deepest nodes in the search tree first.
    e
        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print("Start:", problem.getStartState())
        print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
        print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Creating list and stack
    expandedNodes = []
    frontier = util.Stack()
    # Creating the start node, with the start state, list of actions(empty), and the cost
    firstState = (problem.getStartState(), [], 1)
    # adding the start node to the frontier stack
    frontier.push(firstState)
    while not frontier.isEmpty():
        # destructuring the first element in the frontier stack
        currentState, action, cost = frontier.pop()
        if problem.isGoalState(currentState):
            return action  # if goal is reached return list of actions
        if currentState not in expandedNodes:
            # append current state to expandednodes if not in
            expandedNodes.append(currentState)
            # get succesors of current state
            succesors = problem.getSuccessors(currentState)
            for succ in succesors:  # iterate each succesor
                sState, sAction, sCost = succ  # get state,list of actions and cost
                if sState not in frontier.list and sState not in expandedNodes:
                    # append action to list of actions
                    newAction = action + [sAction]
                    newNode = (sState, newAction, problem.getCostOfActions(
                        newAction))  # create new node,
                    frontier.push(newNode)  # push to frontier

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Creating list and queue
    expandedNodes = []
    frontier = util.Queue()
    # Creating the start node, with the start state, list of actions(empty), and the cost
    firstState = (problem.getStartState(), [], 0)
    # adding the start node to the frontier queue
    frontier.push(firstState)
    while not frontier.isEmpty():
        # destructuring the first element in the frontier stack
        currentState, action, cost = frontier.pop()
        if problem.isGoalState(currentState):
            return action
        if currentState not in expandedNodes:
            # append current state to expandednodes if not in
            expandedNodes.append(currentState)
            # get succesors of current state
            succesors = problem.getSuccessors(currentState)
            for succ in succesors:
                sState, sAction, sCost = succ
                if sState not in frontier.list and sState not in expandedNodes:
                    # append action to list of actions
                    newAction = action + [sAction]
                    # create new node,
                    newNode = (sState, newAction,
                               problem.getCostOfActions(newAction))
                    # push to frontier
                    frontier.push(newNode)

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Creating list and priorityqueue
    expandedNodes = []
    frontier = util.PriorityQueue()
    # Creating the start node, with the start state, list of actions(empty), and the cost
    firstState = (problem.getStartState(), [], 0)
    # adding the start node to the frontier queue
    frontier.push(firstState, 0)
    while not frontier.isEmpty():
        # destructuring the first element in the frontier stack
        currentState, action, cost = frontier.pop()
        if problem.isGoalState(currentState):
            return action
        if currentState not in expandedNodes:
            # append current state to expandednodes if not in
            expandedNodes.append(currentState)
            # get succesors of current state
            succesors = problem.getSuccessors(currentState)
            for succ in succesors:
                sState, sAction, sCost = succ
                if sState not in frontier.heap and sState not in expandedNodes:
                    # append action to list of actions
                    newAction = action + [sAction]
                    newCost = problem.getCostOfActions(newAction)
                    # create new node
                    newNode = (sState, newAction, newCost)
                    # push to frontier
                    frontier.push(newNode, newCost)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Creating list and priorityqueue
    expandedNodes = []
    frontier = util.PriorityQueue()
    # initialize heuristic
    heuristicCost = heuristic(problem.getStartState(), problem)
    # Creating the start node, with the start state, list of actions(empty), and the heuristic cost
    firstState = (problem.getStartState(), [], heuristicCost)
    # adding the start node to the frontier queue
    frontier.push(firstState, 0)
    while not frontier.isEmpty():
        # destructuring the first element in the frontier stack
        currentState, action, cost = frontier.pop()
        if problem.isGoalState(currentState):
            return action
        if currentState not in expandedNodes:
            # append current state to expandednodes if not in
            expandedNodes.append(currentState)
            # get succesors of current state
            succesors = problem.getSuccessors(currentState)
            for succ in succesors:
                sState, sAction, sCost = succ
                if sState not in frontier.heap and sState not in expandedNodes:
                    # append action to list of actions
                    newAction = action + [sAction]
                    newCost = problem.getCostOfActions(newAction)
                    # cualculate f(n) = g(n) + h(n)
                    totalCost = newCost + heuristic(sState, problem)
                    # create new node
                    newNode = (sState, newAction, totalCost)
                    # push to frontier
                    frontier.push(newNode, totalCost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
