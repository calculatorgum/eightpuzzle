#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: meera malhotra
#
#

from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    def __init__(self, board, predecessor, move):
        """new State object by initializing the following four attributes"""
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1

            
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    def is_goal(self):
        """ returns True if the called State object is a goal state, 
        and False otherwise """
        if self.board.tiles == GOAL_TILES:
            return True
        else:
            return False
        
    def generate_successors(self):
        """ creates and returns a list of State objects for all 
        successor states of the called State object"""
        successors = []
        for m in MOVES:
            b = self.board.copy()
            if b.move_blank(m) == True:
                new_obj = State(b, self, m)
                successors.append(new_obj)
        return successors
    
    def print_moves_to(self):
        """ follow predecessor references back up the state-space 
        search tree in order to find and print the sequence of moves"""
        if self.predecessor == None:
            print('Initial State:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print(self.move)
            print(self.board)
     
 
if __name__ == '__main__':
          
    # b1 = Board('142358607')
    # s1 = State(b1, None, 'init')
    # print(s1)
    # b2 = b1.copy()
    # print(b2.move_blank('up'))
    # s2 = State(b2, s1, 'up')    # s1 is the predecessor of s2
    # print(s2)
    
    # s1 = State(Board('102345678'), None, 'init')
    # print(s1.is_goal())
    # s2 = State(Board('012345678'), s1, 'left')
    # print(s2.is_goal())
    
    b1 = Board('142358607')
    print(b1)
    s1 = State(b1, None, 'init')
    print(s1)
    
    succ = s1.generate_successors()   
    print(succ)
    print(s1)
    print(succ[2])
    print(succ[2].generate_successors())
    print(succ[0])
    print(succ[0].generate_successors())
    
    
    
    
    
    
    
    
