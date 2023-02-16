import numpy as np
from dna import *
from gol import *

def glider_fitness(agent, max_frames = 1000, board_dim = (50, 50), starting_pos = (23, 23)):
    score = 0
    
    ## Set up the board
    gol_board = GOL(board_dim)
    gol_board.add_agent(starting_pos, agent)
    
    # Calculate the sum of all values in the board
    av_positions = list()
    while gol_board.next_frame() and gol_board.curr_frame < max_frames:
        if gol_board.curr_frame > 1:
            # calculate the average position?
            #for frame in gol_board.frames:
            pos = [0, 0]
            for m in gol_board.board:
                #print(y)
                for n in gol_board.board[m]:
                    if n == 1:
                        pos[0] += m
                        pos[1] += n
            av_positions.append(pos)
            # or hold all the positional values and see how closely it matches linear movement
        else:
            s = 0
            
        if s > score:
            score = s
            
    return av_positions
    

def explosion_fitness(agent, max_frames = 1000, board_dim = (50, 50), starting_pos = (23, 23)):
    
    score = 0
    
    ## Set up the board
    gol_board = GOL(board_dim)
    gol_board.add_agent(starting_pos, agent)
    
    # Calculate the sum of all values in the board
    while gol_board.next_frame() and gol_board.curr_frame < max_frames:
        if gol_board.curr_frame > 1:
            s = np.sum(gol_board.board) / np.log10(gol_board.curr_frame)
        else:
            s = 0
            
        if s > score:
            score = s
            
    return score
        
def duration_fitness(agent, max_frames = 5000, board_dim = (50, 50), starting_pos = (23, 23)):
    
    ## Set up the board
    gol_board = GOL(board_dim)
    gol_board.add_agent(starting_pos, agent)
    
    # Calculate the sum of all values in the board
    while gol_board.next_frame() and gol_board.curr_frame < max_frames:
        pass
            
    return gol_board.curr_frame
        
