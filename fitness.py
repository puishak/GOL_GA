import numpy as np
from dna import *
from gol import *

def glider_fitness(agent, max_frames = 1000, board_dim = (50, 50), starting_pos = (23, 23)):
    score = 0
    s = 0
    
    ## Set up the board
    gol_board = GOL(board_dim)
    gol_board.add_agent(starting_pos, agent)
    
    # Calculate the sum of all values in the board
    av_positions = list()
    while gol_board.next_frame() and gol_board.curr_frame < max_frames:
        #if gol_board.curr_frame > 0:
        # calculate the average position over frames
        pos = [0, 0] 
        m = 1 
        t = 1
        for r in gol_board.board:
            n = 1
            for c in r:
                if c == 1:
                    pos[0] += m
                    pos[1] += n
                    t += 1
                n += 1
            m += 1
        pos[0] = pos[0]/t
        pos[1] = pos[1]/t
        av_positions.append(pos)
        print(pos)
        # find a way to see how closely the average positions match linear movement
        # probably consider the magnitude of the shift
        
        #for i in range(len(av_positions)):
            
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
        
