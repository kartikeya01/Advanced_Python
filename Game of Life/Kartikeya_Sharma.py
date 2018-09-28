import sys
import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
        You might use this in your createBoard(width, height) function 
    """
    row = []
    for col in range(width):
        row += [0]
    
    return row

def createBoard(width,height):
    """ returns a 2d array of width and height """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    
    return A

def printBoard(A):
    """ this function prints the 2d lost-of-lists
        A without spaces(using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        but, only in the *intereior* of the 2d array
    """
    A = createBoard(width, height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    
    return A
'''
The for loops contaain the 1's and 0's. This way, all
the borders are covered with 0s. The loop says that if
the position of the row and column are equal, the output,
or which number is displayed, will be 1. Otherwise 0.
Thus, the numbers will be 1 when the positions are (1,1),
(2,2), (3,3), etc.
'''
def innerCells(width, height):
    """ returns a 2d array that has all live cells
        except for a one-cell-wide border of empty
        cells around the endge of the 2d array
    """
    A = createBoard(width,height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = 1
    
    return A
'''
The for loops contain the 1's and 0's. This way, all
the borders are covered with 0s. This function tests out
the for loop as all numbers will be one except borders, which
will be 0.
'''
def randomCells(width, height):
    """ returns an array of randomly-assigned 1's and 0's
        except that the outer edge of the array is still
        completely empty (all 0's)
    """
    A = createBoard(width,height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = random.choice( [0, 1] )
    
    return A
'''
The for loops contain the 1's and 0's. This way, all
the borders are covered with 0s. Inside the loop, their is a
statement which randomly assigns either a 1 or a 0 to each
position in the parameters.
'''
def copy(A):
    """ copy will accept a 2d array A as its argument,
        and it will return a new 2d array of data that
        has the same pattern as the original array.
    """
    width = len(A[0])
    height = len(A)
    newA = createBoard( width, height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            newA[row][col] = A[row][col]
    
    return newA
'''
The for loops contain the 1's and 0's. This way, all
the borders are covered with 0s. This copy funtion will
make a newA which is also a createboard from the previous
A. It returns the new positions in the board. This function
is very helpful for later functions.
'''
def innerReverse(A):
    ''' takes an old 2d array (or "generation") and
        then creates a new generation of the same shape
        and size. However, the new generation should
        be the "opposite" of A's cells everywhere except
        on the outer edge.
    '''
    width = len(A[0])
    height = len(A)
    newA = copy(A)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    
    return newA
'''
The for loops contain the 1's and 0's. This way, all
the borders are covered with 0s. By creating an if statement,
I was able to say that if the value of the poistion in createboard A
is >0 (or 1), then change the value of the newA to 0. Otherwise, make
newA equal to 1. This makes each value opposite. 
'''
def countNeighbors(row, col, A):
    ''' it should return the number of live neighbors
        for a cell in the board A at a particular row
        and col.
    '''
    Neighbor = 0
    
    if A[row][col+1] == 1:
        Neighbor = Neighbor +1
    if A[row-1][col+1] == 1:
        Neighbor = Neighbor +1
    if A[row-1][col] == 1:
        Neighbor = Neighbor +1
    if A[row-1][col-1] == 1:
        Neighbor = Neighbor +1
    if A[row][col-1] == 1:
        Neighbor = Neighbor +1
    if A[row+1][col-1] == 1:
        Neighbor = Neighbor +1
    if A[row+1][col] == 1:
        Neighbor = Neighbor +1
    if A[row+1][col+1] == 1:
        Neighbor = Neighbor +1

    return Neighbor
'''
We don't need to worry about the for loops in this
funstion as it only cares for the values touching it,
within a radius of 1. So only eight values are needed.
Everytime the value of one of the eight positions is 1,
Neighbors = Neigbors + 1. Neighbors is returned for this
function.
'''
def next_life_generation(A):
    """ makes a copy of A and then advances one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. The outer 
        edge always stays at 0. 
    """ 
    width = len(A[0])
    height = len(A)
    newA = copy(A)    
    for row in range(1, height-1):
        for col in range(1, width-1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            if countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            if A[row][col] == 0 and countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            
    return newA
'''
The for loops contain the 1's and 0's. This way, all
the borders are covered with 0s. This serves as the rulebook
for the Game of Life. If there are less than two neighbors, the newA
becomes a 0. If there are more than three neighbors, the newA becomes 0.
If the previous board is 0 and there are exactly three neighbors, the new
board, newA, produces an output of 1.
'''