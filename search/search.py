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
from util import Stack
from util import Queue
from util import PriorityQueue
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #  	  print "Start:", problem.getStartState()
	#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
    Stack_1=Stack()
    result=Stack()
    curr_state=problem.getStartState()
    Stack_1.push(curr_state)
    answer=[]
    parent={curr_state:None}
    direction={curr_state:None}
    visited={curr_state:True}
    while(Stack_1.isEmpty()==False and problem.isGoalState(curr_state)==False):
        curr_state=Stack_1.pop()
        for succ,action,cost in problem.getSuccessors(curr_state):
            if visited.has_key(succ)==False:
                visited[succ]=True
                direction[succ]=action
                parent[succ]=curr_state
                Stack_1.push(succ)
    if problem.isGoalState(curr_state)==True:
        while(parent[curr_state]!=None):
	        result.push(direction[curr_state])
	        curr_state=parent[curr_state]
   # result.pop()
    while(result.isEmpty==False):
	    answer.append(result.pop())
    return answer
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    source=problem.getStartState()
    visited={source:True}
    parent={source:None}
    direction={source:None}
    q=Queue()
    q.push(source)
    s=Stack()
    while(q.isEmpty()==False and problem.isGoalState(source)==False):
        source=q.pop()
        for succ,action,cost in problem.getSuccessors(source):
            if visited.has_key(succ)==False:
                visited[succ]=True
                parent[succ]=source
                direction[succ]=action
                q.push(succ)
    if problem.isGoalState(source)==True:
        while(parent[source]!=None):
            s.push(direction[source])
            source=parent[source]
    result=[]
    while(s.isEmpty()==False):
        result.append(s.pop())
    return result
#     source=problem.getStartState()
#     count=0
#     parent={source:None}
#     while(count<4):
#         visited={source:True}
#         direction={source:None}
#         q=Queue()
#         q.push(source)
#         s=Stack()
#         while(q.isEmpty()==False and problem.isGoalState(source)==False):
#             source=q.pop()
#             for succ,action,cost in problem.getSuccessors(source):
#                 if visited.has_key(succ)==False:
#                     visited[succ]=True
#                     parent[succ]=source
#                     direction[succ]=action
#                     q.push(succ)
#         count+=1
#     #if problem.isGoalState(source)==True:
#     while(parent[source]!=None):
#         s.push(direction[source])
#         source=parent[source]
#     result=[]
#     while(s.isEmpty()==False):
#         result.append(s.pop())
#     return result
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    source=problem.getStartState()
    distance={source:0}
    parent={source:None}
    direction={source:None}
    Q=PriorityQueue()
    s=Stack()
    Q.push(source,0)
    while(Q.isEmpty()==False and problem.isGoalState(source)==False):
        source=Q.pop()
        for succ,action,cost in problem.getSuccessors(source):
            if distance.has_key(succ)==True:
                if distance[succ]>cost+distance[source]:
                    distance[succ]=cost+distance[source]
                    parent[succ]=source
                    direction[succ]=action
            else:
                distance[succ]=distance[source]+cost
                parent[succ]=source
                direction[succ]=action
                Q.push(succ,distance[source]+cost)
    if problem.isGoalState(source)==True:
        while(parent[source]!=None):
            s.push(direction[source])
            source=parent[source]
    result=[]
    while(s.isEmpty()==False):
        result.append(s.pop())
    return result
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
#     source=problem.getStartState()
#     distance={source:0}
#     total={source:0}
#     parent={source:None}
#     direction={source:None}
#     Q=PriorityQueue()
#     s=Stack()
#     Q.push(source,heuristic(source,problem))
#     while(Q.isEmpty()==False and problem.isGoalState(source)==False):
#         source=Q.pop()
#         for succ,action,cost in problem.getSuccessors(source):
#             if total.has_key(succ)==True:
#                 if total[succ]>cost+distance[source]+heuristic(succ,problem):
#                     total[succ]=cost+distance[source]+heuristic(succ,problem)
#                     distance[succ]=cost+distance[source]
#                     parent[succ]=source
#                     direction[succ]=action
#                 else:
#                     total[succ]=distance[source]+cost+heuristic(succ,problem)
#                     distance[succ]=distance[source]+cost
#                     parent[succ]=source
#                     direction[succ]=action
#                     Q.push(succ,total[succ])
#     if problem.isGoalState(source)==True:
#         while(parent[source]!=None):
#             s.push(direction[source])
#             source=parent[source]
#     result=[]
#     while(s.isEmpty()==False):
#         result.append(s.pop())
#     return result
    source=problem.getStartState()
    distance={source:0}
    parent={source:None}
    direction={source:None}
    Q=PriorityQueue()
    s=Stack()
    Q.push(source,heuristic(source,problem))
    while(Q.isEmpty()==False and problem.isGoalState(source)==False):
        source=Q.pop()
        for succ,action,cost in problem.getSuccessors(source):
            if distance.has_key(succ)==True:
                if distance[succ]>cost+distance[source]+heuristic(succ,problem):
                    distance[succ]=cost+distance[source]+heuristic(succ,problem)
                    parent[succ]=source
                    direction[succ]=action
            else:
                distance[succ]=distance[source]+cost+heuristic(succ,problem)
                parent[succ]=source
                direction[succ]=action
                Q.push(succ,distance[source]+cost+heuristic(succ,problem))
    if problem.isGoalState(source)==True:
        while(parent[source]!=None):
            s.push(direction[source])
            source=parent[source]
    result=[]
    while(s.isEmpty()==False):
        result.append(s.pop())
    return result
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
