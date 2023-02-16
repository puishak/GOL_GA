import cv2 as cv
import numpy as np
from dna import *
from gol import *
from fitness import *


def animate_board(gol, frame_rate = 10):
    rootWindow = "  --  GAME OF LIFE!!  --  "
    cv.namedWindow(rootWindow)

    scale_factor = np.int32(1000 / gol.dim[0])
    
    
    while True:
        key = cv.waitKey(np.int32(1000/frame_rate))

        img = gol.board.copy()
        img = img * 255
        img = img.astype(np.uint8)
        
        for i in range(int(np.log2(scale_factor))):

            img = np.repeat(np.repeat(img, 2, axis=0), 2, axis=1)

        cv.imshow(rootWindow, img)

        if not gol.next_frame() or key == 32:
            break
    cv.destroyAllWindows()
    
    
if __name__ == "__main__":
    board_dimention = (50, 50)
    agent_dim = (4, 4)
    starting_pos = (23, 23)
    

    # Create the game of life baord
    gol_board = GOL(board_dimention)

    # Create a random agent
    agent = DNA(agent_dim)
    # Define the position we would like to place the agent
    gol_board.add_agent(starting_pos, agent)


    # mat = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
    # gol_board.modify((5, 5), mat)

    animate_board(gol_board, frame_rate = 30)
    
    print(explosion_fitness(agent, board_dim=board_dimention, starting_pos=starting_pos))

    