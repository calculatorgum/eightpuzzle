#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: meera malhotra
# email: meeram@bu.edu
#
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        for r in range(0, 3):
            for c in range(0, 3):
                self.tiles[r][c] = int(digitstr[3*r + c])
                
                if(self.tiles[r][c] == 0):
                    self.blank_r = r
                    self.blank_c = c


    def __repr__(self):
        """ constructs, each numeric tile should be represented by 
        the appropriate single-character string, 
        followed by a single space """
        
        string = ''
        for r in range(0, 3):
            for c in range(0, 3):
                if self.tiles[r][c] == 0:
                    string += '_' + ' '
                else:
                    string += str(self.tiles[r][c]) + ' '
            string += '\n'
        
        return string
        
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the 
        direction in which the blank should move, and that attempts 
        to modify the contents of the called Board object accordingly """
        
        assert(direction in ['up', 'down', 'left', 'right'])

        row = 0
        col = 0
        
        if direction == 'up':
            row = self.blank_r - 1
            col = self.blank_c
            if row < 0 or row > 2:   #doesn't allow the space to move past bounds
                return False
        
        elif direction == 'down':
            row = self.blank_r + 1
            col = self.blank_c
            if row < 0 or row > 2:
                return False
            
        elif direction == 'left':
            row = self.blank_r
            col = self.blank_c - 1
            if col < 0 or col > 2:
                return False
            
        elif direction == 'right':
            row = self.blank_r
            col = self.blank_c + 1
            if col < 0 or col > 2:
                return False
    
        else:
            print('unknown direction')
            return False
        
        
        self.tiles[self.blank_r][self.blank_c] = self.tiles[row][col]
        self.tiles[row][col]= 0
        self.blank_r = row
        self.blank_c = col
        return True
    
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds 
        to the current contents of the called Board object’s 
        tiles attribute """
        string = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                string += str(self.tiles[r][c])
        return string
 
    
    def copy(self):
        """returns a newly-constructed Board object that is a 
        deep copy of the called object"""
        copy = Board(self.digit_string())
        return copy
  
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
        object that are not where they should be in the goal state """
        count = 0
        correct_board = [[0,1,2], [3,4,5], [6,7,8]]
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c] == 0:
                    count += 0
                elif self.tiles[r][c] == correct_board[r][c]:
                    count += 0
                else:
                    count += 1
        return count
        
    
    def __eq__(self, other):
        """ returns True if the called object and the argument have the
        same values for the tiles attribute, and False otherwise"""
        return self.tiles == other.tiles
        
    
    def taxicab(self):
        """finds distance between each space on self board and goal board"""
        count = 0
        correct_board = [[0, 1, 2], [3,4,5], [6,7,8]]
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                count += abs(self.tiles[r][c] - correct_board[r][c])
        return count
        
        
if __name__ == '__main__':
    
    # b = Board('142358607')
    # print(b.tiles)

    # print(b.blank_r)
    # print(b.blank_c)

    b = Board('142358607')
    print(b)
    
    # print(b.move_blank('up'))
    # print(b)
    # print(b.tiles)
    # print(b.blank_r)
    # print(b.blank_c)
    # print(b.move_blank('left'))
    # print(b)
    # print(b.move_blank('down'))
    # print(b)
    # print(b.move_blank('right'))
    # print(b)
    # print(b.move_blank('RIGHT'))


    # print(b.move_blank('right'))
    # print(b)

    #print(b.digit_string())
    #c = Board('012345678')

    #print(b.num_misplaced())      # 1,4,5,7,8 tiles are out of place

    #c = Board('143258607')
    #print(c.num_misplaced())
        
    #c = Board('143258607')    
    #print(c.taxicab())
    
    #c = Board('012345678')
    #print(c.taxicab())
        
        
        
