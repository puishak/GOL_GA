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
        """_summary_

        Args:
            rate (_type_): _description_
        """
        pass
    
    def crossover(self, other):
        child = DNA(self)
        child.dna[-1] = other.dna[-1]
        return child
    
    
    
    
        
        
        
        