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
    
def accept_reject(population):
    pool = list(population.keys())
    total_fitness =  np.sum(list(population.values()))
    
    safe = 0
    while True:
        
        agent = np.random.choice(pool)
        
        r = np.random.rand() * total_fitness
        
        if r < population[agent]:
            return agent
        
        safe += 1
        if safe > 10000:
            print("something wrong in the accept-reject")
            return agent

def next_generation(population, population_size = 100, mutation_rate = 0.01):
    new_population = {}
    
    for i in range(population_size):
        parent1 = accept_reject(population)
        parent2 = accept_reject(population)
        
        child = parent1.crossover(parent2)
        child.mutate(mutation_rate)
                
        new_population[child] = 0
        
    return new_population

def train_explosion():
    board_dim = (50, 50)
    agent_dim = (4, 4)
    starting_pos = (23, 23)
    
    best_of_each_gen = []
    num_generation = 5
    
    # Create the population
    num_agents = 100
    # population: [(agent:DNA, score:int)]
    population = {}
    # Create the initial population
    for i in range(num_agents):
        agent = DNA(agent_dim)
        score = 0
        population[agent] = score
        
    for i in range(num_generation):
        print("Generation: ", i)
        best_agent = (None, 0)    
        
        # Score the population
        ## Hook this up to the distributive end
        for agent in population.keys():
            score = explosion_fitness(agent, board_dim=board_dim, starting_pos=starting_pos)
            population[agent] = score
            if score > best_agent[1]:
                best_agent = (agent, score)
        ## Distributive end
        
        best_of_each_gen.append(best_agent[0])

        # print(population)
        
        population = next_generation(population)
    
    return best_of_each_gen

if __name__ == "__main__":
    board_dim = (50, 50)
    agent_dim = (4, 4)
    starting_pos = (23, 23)
    
    agents = train_explosion()
    
    
    for agent in agents:
        
        # Create the game of life baord 
        gol_board = GOL(board_dim)

        # Create a random agent
        # Define the position we would like to place the agent
        gol_board.add_agent(starting_pos, agent)

        animate_board(gol_board, frame_rate = 10)


    
    # print(explosion_fitness(agent, board_dim=board_dim, starting_pos=starting_pos))

    