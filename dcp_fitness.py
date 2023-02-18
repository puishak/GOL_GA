def dcp_fitness(input):
    import numpy as np
    # Agent here is not an DNA object, but just a numpy matrix
    agent, max_frames, board_dim, starting_pos = input
    
    class GOL:
        def __init__(self, dim) -> None:
            self.dim = dim
            self.board = np.zeros(dim)
            self.curr_frame = 0
            self.frames = []
        
        def add_agent(self, pos, agent_dna):
            start_row = pos[0]
            end_row = start_row + agent_dna.shape[0]
            start_col = pos[1]
            end_col = start_col + agent_dna.shape[1]
            # replace the specified part of the original matrix with the new matrix
            self.board[start_row:end_row, start_col:end_col] = agent_dna
        
        score = 0
        
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
    
    ## paste you fitness function down below
    
    ### Explosion fitness ###
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
    
    
    