import numpy as np
from core.base_algorithm import TSPAlgorithm


class ClassicGA(TSPAlgorithm):

    def __init__(self, problem, pop_size=100, iterations=500,
                 pc=0.8, pm=0.2, seed=None):
        super().__init__(problem, seed)
        self.pop_size = pop_size
        self.iterations = iterations
        self.pc = pc
        self.pm = pm

    def _init_population(self):
        dim = self.problem.distance_matrix.shape[0]
        pop = []
        for _ in range(self.pop_size):
            tour = list(range(1, dim + 1))
            np.random.shuffle(tour)
            pop.append(tour)
        return pop

    def run(self):
        self._start_timer()

        population = self._init_population()

        for _ in range(self.iterations):

            distances = [
                self.problem.calculate_tour_length(ind)
                for ind in population
            ]

            best_idx = np.argmin(distances)

            if distances[best_idx] < self.best_distance:
                self.best_distance = distances[best_idx]
                self.best_tour = population[best_idx].copy()

            self.history.append(self.best_distance)

            # Aquí va tu lógica de selección, cruce y mutación
            # (exactamente la misma que ya tienes)

        self._stop_timer()
        return self