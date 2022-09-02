#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: meera malhotra
# email: meeram@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """

    def __init__(self, depth_limit):
        """ that constructs a new Searcher object by initializing the
        following attributes"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self."""

        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def should_add(self, state): 
        """ takes a State object called state and returns True if the
        called Searcher should add state to its list of untested states, 
        and False otherwise """
        if state.num_moves > self.depth_limit and self.depth_limit > -1:
            return False
        elif state.creates_cycle():
            return False
        else:
            return True
    
    def add_state(self, new_state):
        """ adds takes a single State object called new_state 
        and adds it to the Searcher‘s list of untested states """
        self.states += [new_state]
        
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes
        the elements of new_states """
        for state in new_states:
            if self.should_add(state) == True:
                self.add_state(state)                
        
    def next_state(self):
      """ chooses the next state to be tested from the list of 
         untested states, removing it from the list and returning it
      """
      s = random.choice(self.states)
      self.states.remove(s)
      return s
    
    def find_solution(self, init_state):
        """ performs a full random state-space search, stopping 
        when the goal state is found or when the Searcher runs out
        of untested states """
        self.add_state(init_state)
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())

    
class BFSearcher(Searcher):
    """for searcher objects that perform breadth-first search (BFS) 
    instead of random search"""
    def next_state(self):
        state = self.states[0]
        self.states.remove(state)
        return state
    
class DFSearcher(Searcher):
    """for searcher objects that perform breadth-first search (DFS) instead
    of random search"""
    def next_state(self):
        state = self.states[-1]
        self.states.remove(state)
        return state

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """ heuristic that returns number of misplaced tiles on board """
    heu = state.board.num_misplaced()
    return heu

def h2(state):
    """ heuristic that finds the distance between each place on self board
    and goal board"""
    heu = state.board.taxicab()
    return heu
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
        inputs:
         * depth_limit - the depth limit of the searcher
         * heuristic - a reference to the function that should be used 
         when computing the priority of a state
         """
        super().__init__(depth_limit)  
        self.heuristic = heuristic

    def priority(self, state):
        """takes a State object called state, and that computes 
        and returns the priority of that state"""
        prio = -1 * self.heuristic(state)
        return prio

    def add_state(self, state):
        """ overrides the add_state method that is inherited from Searcher"""
        self.states += [[self.priority(state), state]]
    
    def next_state(self):
        """ overrides the next_state method 
        that is inherited from Searcher """
        closestState = max(self.states)
        self.states.remove(closestState)
        return closestState[-1]
       
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


class AStarSearcher(GreedySearcher):
    """ A* is an informed search algorithm that assigns a priority
    to each state based on a heuristic function, and that selects 
    the next state based on those priorities """
    
    def priority(self, state):
        """assigns a priority to each state based on a heuristic 
        function, and that selects the next state 
        based on those priorities"""
        priority = -1 * (self.heuristic(state) + state.num_moves)
        return priority


if __name__ == '__main__':

    # searcher1 = Searcher(-1)    # -1 means no depth limit
    # print(searcher1)
    # searcher2 = Searcher(10)
    # print(searcher2)
    
    # b1 = Board('142358607')
    # s1 = State(b1, None, 'init')  # initial state
    # searcher1 = Searcher(-1)  # no depth limit
    # searcher1.add_state(s1)
    # searcher2 = Searcher(1)   # depth limit of 1 move!
    # searcher1.add_state(s1)
    # b2 = b1.copy()
    # print(b2.move_blank('left'))
    
    # s2 = State(b2, s1, 'left')    # s2's predecessor is s1
    # print(searcher1.should_add(s2))
    # print(searcher2.should_add(s2))
    
    # b3 = b2.copy()
    # print(b3.move_blank('right'))       # get the same board as b1 
    # s3 = State(b3, s2, 'right')   # s3's predecessor is s2
    # print(searcher1.should_add(s3))     # adding s3 would create a cycle
    # print(searcher2.should_add(s3))
    
    # print(b3.move_blank('left'))        # reconfigure b)
    # print(b3.move_blank('up'))


    # s3 = State(b3, s2, 'up')      # recreate s3 with new b3 (no cycle)
    # print(s3.num_moves)
    # print(searcher1.should_add(s3))      # searcher1 has no depth limit
    # print(searcher2.should_add(s3))     # s3 is beyond searcher2's depth limit
    
    # b = Board('142358607')
    # s = State(b, None, 'init')
    # searcher = Searcher(-1)
    # searcher.add_state(s)
    # print(searcher.states)  
    
    # succ = s.generate_successors()
    # print(succ)
    # searcher.add_state(succ[0])  # add just the first successor
    # print(searcher.states)
    
    # b = Board('142358607')
    # s = State(b, None, 'init')
    # searcher = Searcher(-1)
    # searcher.add_state(s)
    # print(searcher.states)
    # succ = s.generate_successors()
    # print(succ)
    # searcher.add_states(succ)             # add all of the successors
    # print(searcher.states)
    # print(succ[-1])
    # succ2 = succ[-1].generate_successors() 
    # print(succ2)
    # searcher.add_states(succ2)
    # print(searcher.states)
    
    # b = Board('012345678')       # the goal state!
    # s = State(b, None, 'init')   # start at the goal
    # print(s)
    # searcher = Searcher(-1)
    # print(searcher)
    # print(searcher.find_solution(s))    # returns init state, because it's a goal state
    # print(searcher)
    
    # b = Board('142358607')       
    # s = State(b, None, 'init')   
    # print(s)
    # searcher = Searcher(-1)
    # print(searcher)
    # print(searcher.find_solution(s))   # returns goal state at depth 11
    
    # print(searcher)
    # searcher = Searcher(-1)   # a new searcher with the same init state
    # print(searcher)
    # print(searcher.find_solution(s))    # returns goal state at depth 5
    # print(searcher)

    # b = Board('142305678')    # only 2 moves from a goal
    # print(b)
    # s = State(b, None, 'init')   
    # searcher = Searcher(-1)
    # goal = searcher.find_solution(s)
    # print(goal)
    # goal.print_moves_to()

    # b = Board('142358607')       
    # s = State(b, None, 'init')
    # print(s)
    # bfs = BFSearcher(-1)
    # bfs.add_state(s)
    # print(bfs.next_state())    # remove the initial state
    # succ = s.generate_successors()
    # print(succ)
    # bfs.add_states(succ)
    # bfs.next_state()
    # print(bfs.next_state())

    # b = Board('142358607')       
    # s = State(b, None, 'init')
    # print(s)
    # dfs = DFSearcher(-1)
    # dfs.add_state(s)
    # print(dfs.next_state())     # remove the initial state
    # succ = s.generate_successors()
    # print(succ)
    # dfs.add_states(succ)
    # print(dfs.next_state())   # the last one added, not the first!
    # print(dfs.next_state())

    # b = Board('142358607')       
    # s = State(b, None, 'init')
    # g = GreedySearcher(-1, h1)
     # print(g)
    
#     b = Board('142358607')       
#     s = State(b, None, 'init')
#     g = GreedySearcher(-1, h1)
#     g.add_state(s)
#     print(g.states)
# #[[-5, 142358607-init-0]]
#     succ = s.generate_successors()
#     g.add_state(succ[0])
#     print(g.states)
# #[[-5, 142358607-init-0], [-5, 142308657-up-1]]
#     g.add_state(succ[1])
#     print(g.states)
# #[[-5, 142358607-init-0], [-5, 142308657-up-1], [-6, 142358067-left-1]]

#     b = Board('142358607')       
#     s = State(b, None, 'init')
#     g = GreedySearcher(-1, h1)  # no depth limit, basic heuristic
#     g.add_state(s)
#     succ = s.generate_successors()
#     g.add_state(succ[1])
#     print(g.states)
# #[[-5, 142358607-init-0], [-6, 142358067-left-1]]
#     print(g.next_state())    # -5 is the higher priority
# #142358607-init-0

#     print(g.states)
# #[[-6, 142358067-left-1]]


    b = Board('142358607')       
    s = State(b, None, 'init')
    a = AStarSearcher(-1, h1)  # no depth limit, basic heuristic
    a.add_state(s)
    print(a.states)          # init state has same priority as in greedy
#[[-5, 142358607-init-0]]
    succ = s.generate_successors()
    a.add_state(succ[1])
    print(a.states)         # succ[1] has a priority of -1*(6 + 1) = -7
#[[-5, 142358607-init-0], [-7, 142358067-left-1]]
    print(a.next_state())   # -5 is the higher priority
#142358607-init-0
    print(a.states)
#[[-7, 142358067-left-1]]



    # b = Board('142358607')    # only 2 moves from a goal
    # print(b)
    # s = State(b, None, 'init')   
    # searcher = GreedySearcher(-1, h1)
    # goal = searcher.find_solution(s)
    # print(goal)
    # goal.print_moves_to()
    













