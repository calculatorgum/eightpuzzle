#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: meera malhotra
# email: meeram@bu.edu
#


from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher


def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
            
def process_file(filename, algorithm, depth_limit = -1, heuristic= None):
    """ processes text file and prints averages for different algorithms"""
    file = open(filename, 'r')
    num_puzz = 0
    num_moves = 0
    num_tested = 0
    
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        algorithm = str(algorithm)
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        
        soln = None
        try:
            soln = searcher.find_solution(init_state)
           
            if soln == None:
                print(line + ':', 'no solution')
        
            else:
                num_puzz += 1
                num_moves += soln.num_moves
                num_tested += searcher.num_tested
                print(line + ':', soln.num_moves,'moves,', searcher.num_tested, 'states tested')
                
        
        except KeyboardInterrupt:
            print('search terminated ', end='')
            soln = None

    print ()

    if num_puzz > 0:
        print ('solved', num_puzz, 'puzzles')
        average_moves = num_moves / num_puzz
        average_tests = num_tested / num_puzz
        print('averages:', average_moves, 'moves', average_tests, 'states tested')
    else:
        print('solved 0 puzzles')
    file.close()




#process_file('15_moves.txt', 'Greedy', -1, h1)   

#s1 = create_searcher('BFS', -1, None)
#print(s1)
# print(eight_puzzle('142358607', 'random', -1))
#print(eight_puzzle('142358607', 'BFS', -1))
#print(eight_puzzle('142358607', 'DFS', -1))

#print(eight_puzzle('142358607', 'Greedy', -1, h1))
#print(eight_puzzle('142358607', 'A*', -1, h1))

