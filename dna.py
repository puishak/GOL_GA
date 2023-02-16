import numpy as np

class DNA:
    
    
    def __init__(self, shape, mode = "random"):
        """return a DNA with the DNA_size
        MODES:
            "dead" - Initiate all cell to 0
            "alive" - Initiate all cell to 1
            "Random" - Initiate all cell randomly to either 0 or 1
            

        Args:
            DNA_size (_type_): _description_
            mode (str, optional): _description_. Defaults to "False".
        """ 
        if mode == "random":
            self.dna = np.random.randint(2, size=shape)
        elif mode == "dead":
            self.dna = np.zeros(shape)
        elif mode == "alive":
            self.dna = np.ones(shape)
    
        
    
    def mutate(self, rate):
        for i in range(self.dna.shape[0]):
            for j in range(self.dna.shape[1]):
                # randomly flip the value with 1% probability
                if np.random.rand() < rate:
                    self.dna[i, j] = 1 - self.dna[i, j]
        
    
    def crossover(self, other):
        
        if self.dna.shape != other.dna.shape:
            return -1
        
        child = DNA(self.dna.shape, mode = "dead")
        
        shape = self.dna.shape
        child.dna = self.dna
        
        start_row = np.random.randint(shape[0])
        start_col = np.random.randint(shape[1])

        if start_row >= 0 and start_col >= 0:
            child.dna[start_row:, start_col:] = other.dna[start_row:, start_col:]
        
        end_row = np.random.randint(shape[0])
        end_col = np.random.randint(shape[1])

        if start_row >= 0 and start_col >= 0:
            child.dna[:end_row, :end_col] = other.dna[:end_row, :end_col]
        
        return child
    
    
    
    
        
        
        
        