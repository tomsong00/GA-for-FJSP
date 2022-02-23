class Parameters(object):
    def __init__(self):
        self.beta = None
        self.alpha =None
        self.population_size = None
        self.max_generation = None
        self.length=None
        self.gobal_best_fitness=None


    def parameter_setting(self):
        self.max_generation = 30
        self.population_size = 10
        self.alpha = 0.9
        self.beta = 0.1
        self.length=3
        self.gobal_best_fitness=9999
        return self.max_generation, self.population_size, self.alpha, self.beta, self.gobal_best_fitness,self.length
