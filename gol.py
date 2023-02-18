import numpy as np
from dna import *

class GOL:    
    def __init__(self, dim) -> None:
        self.dim = dim
        self.board = np.zeros(dim)
        self.curr_frame = 0
        self.frames = []
    
    def add_agent(self, pos, agent):
        self.modify(pos, agent.dna)
        
    
    def modify(self, pos, mat):
        # pos is the top left corner of the matrix
        # mat is the matrix of True/False that is to be added on top of the current board

        start_row = pos[0]
        end_row = start_row + mat.shape[0]
        start_col = pos[1]
        end_col = start_col + mat.shape[1]

        if start_row >= 0 and start_col >= 0 and end_row <= self.board.shape[0] and end_col <= self.board.shape[1]:
            # replace the specified part of the original matrix with the new matrix
            self.board[start_row:end_row, start_col:end_col] = mat
            return 1
        else:
            return -1
        
        
        
        
    
    def next_frame(self):
        
        # Count the number of alive neighbors for each cell
        neighbors = np.zeros_like(self.board)
        neighbors[1:,1:] += self.board[:-1,:-1]
        neighbors[1:,:-1] += self.board[:-1,1:]
        neighbors[:-1,1:] += self.board[1:,:-1]
        neighbors[:-1,:-1] += self.board[1:,1:]
        neighbors[:-1,:] += self.board[1:,:]
        neighbors[1:,:] += self.board[:-1,:]
        neighbors[:,:-1] += self.board[:,1:]
        neighbors[:,1:] += self.board[:,:-1]

        # Apply the rules of the game
        new_board = np.logical_or(
            np.logical_and(self.board, np.logical_or(neighbors == 2, neighbors == 3)),
            np.logical_and(np.logical_not(self.board), neighbors == 3)
        ).astype(int)
        
        flag = self.repeating()
        self.board = new_board
        self.curr_frame += 1
        
        return flag
        
        
    def repeating(self):
        # returns true if the board has started to repeat itself
        output = True
        
        for frame in self.frames:
            if (frame == self.board).all():
                output = False
        
        if len(self.frames) > 10:
            self.frames.pop(0)
            
        self.frames.append(self.board.copy())
        
        return output
        
