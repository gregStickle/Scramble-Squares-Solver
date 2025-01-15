import math
from itertools import permutations
from typing import List
import time

def printBoard(board):
    print(f"[{board[0]}, {board[1]}, {board[2]}]") 
    print(f"[{board[3]}, {board[4]}, {board[5]}]") 
    print(f"[{board[6]}, {board[7]}, {board[8]}]\n") 

class Piece:
    def __init__(self, id, sides):
        self.id = id
        self.originalSides: str = sides
        self.currentSides: str = self.originalSides
        self.orientation: int = 0
        self.top: str = sides[0]
        self.right: str = sides[1]
        self.bottom: str = sides[2]
        self.left: str = sides[3]

    def setOrientation(self, newOrienation: int):
        # Update current orienation
        self.orientation = newOrienation
        # Update currentSides based on orientation
        if self.orientation == 0:
            self.currentSides = str(self.originalSides[0] + self.originalSides[1] + self.originalSides[2] + self.originalSides[3])
        elif self.orientation == 1:
            self.currentSides = str(self.originalSides[3] + self.originalSides[0] + self.originalSides[1] + self.originalSides[2])
        elif self.orientation == 2:
            self.currentSides = str(self.originalSides[2] + self.originalSides[3] + self.originalSides[0] + self.originalSides[1])
        else:
            self.currentSides = str(self.originalSides[1] + self.originalSides[2] + self.originalSides[3] + self.originalSides[0])

        self.top: str = self.currentSides[0]
        self.right: str = self.currentSides[1]
        self.bottom: str = self.currentSides[2]
        self.left: str = self.currentSides[3]

        # if orienation = 0, then sides=[1,2,3,4]
        # Update top,right,bottom,left
        

    def __str__(self):
        return f"Piece: {self.id} Orientation: {self.orientation}"

def checkBoard(board):
    piece1:Piece = board[0]
    piece2:Piece = board[1]
    piece3:Piece = board[2]
    piece4:Piece = board[3]
    piece5:Piece = board[4]
    piece6:Piece = board[5]
    piece7:Piece = board[6]
    piece8:Piece = board[7]
    piece9:Piece = board[8]
    
    # Horizontal Check
    if not doSidesMatch(piece1.right, piece2.left): return 2
    if not doSidesMatch(piece2.right, piece3.left): return 3
    if not doSidesMatch(piece1.bottom, piece4.top): return 4
    if not doSidesMatch(piece4.right, piece5.left): return 5
    if not doSidesMatch(piece2.bottom, piece5.top): return 5
    if not doSidesMatch(piece5.right, piece6.left): return 6
    if not doSidesMatch(piece3.bottom, piece6.top): return 6
    if not doSidesMatch(piece4.bottom, piece7.top): return 7
    if not doSidesMatch(piece7.right, piece8.left): return 8
    if not doSidesMatch(piece5.bottom, piece8.top): return 8
    if not doSidesMatch(piece6.bottom, piece9.top): return 9
    if not doSidesMatch(piece8.right, piece9.left): return 9

    # Vertical Check



    # If all matches, solution found
    return 0

def doSidesMatch(side1: str, side2: str):
    # Definitions of a match
    # A,a OR a,A
    # B,b OR b,B
    # C,c OR c,C
    # D,d OR d,D
    if (side1 == 'A' and side2 == 'a'): return True
    if (side1 == 'a' and side2 == 'A'): return True
    if (side1 == 'B' and side2 == 'b'): return True
    if (side1 == 'b' and side2 == 'B'): return True
    if (side1 == 'C' and side2 == 'c'): return True
    if (side1 == 'c' and side2 == 'C'): return True
    if (side1 == 'D' and side2 == 'd'): return True
    if (side1 == 'd' and side2 == 'D'): return True
    # Not one of valid matches defined above
    return False
    
def iterateOrientation(currentOrientation: str, bit: int):
    # Convert bit to power
    power = 9 - bit
    # Get value from string
    intOrientation = int(currentOrientation,4)
    # Iterate
    intOrientation += int(1 * math.pow(4,power))
    # Convert to base 4
    newOrientation = ""
    while intOrientation > 0:
        newOrientation = str(intOrientation % 4) + newOrientation
        intOrientation //= 4
    
    while len(newOrientation) < 9:
        newOrientation = "0" + newOrientation
    # return
    return newOrientation

def setOrientations(board, orientation: str):
    for piece in board:
        piece.setOrientation(int(orientation[0]))
        orientation = orientation[1:]

def buildBoard():
    # OR Come up with a new way to store available pieces
    # Aka instead of [1,2,3,4,5,6,7,8,9] do
    # [1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, ...]
    # And then figure out a way to get one each?


    # Could build a rotatePieces function that increments a 9 bit base 4 numeral
    # by 1 where each bit represents the rotation of a piece.

    # Build each possible permutation of piece location
    solved = False
    perms=list(permutations(pieces))
    for perm in perms:
        orientationPerm="000000000"
        while int(orientationPerm) < 333333333:
            #print(f"OrientationPerm {orientationPerm}")
            setOrientations(perm, orientation=orientationPerm)
            result = checkBoard(perm)
            if result == 0:
                # Solution found
                printBoard(perm)
                print("Solution found!")
                solved=True 
                break
            orientationPerm=iterateOrientation(currentOrientation=orientationPerm, bit=result)
        if solved: break
        #print("Time for a new board!")
        #startTime = time.time()
        # Build each possible rotation of each piece


        #if checkBoard(perm): 
        #    print("Solution Found")
        #    break
        #print("Not a solution. \n")
    
    print(f"----- {time.time() - startTime} seconds -----")

def getBoardPieces():
    print(" ----- Board Input ----- ")
    print(" Example sides = aDcB ")
    pieces = []
    for i in range(1,10):
        sides = input(f"Enter sides of square {i}: ")
        pieces.append(Piece(i, sides))
    return pieces

pieces = getBoardPieces()
board = []

startTime = time.time()
buildBoard()
