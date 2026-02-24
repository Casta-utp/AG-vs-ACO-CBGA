import numpy as np
from core.base_algorithm import TSPAlgorithm


class CBGA(TSPAlgorithm):

    def __init__(self, problem,
                 pop_size=100,
                 iterations=500,
                 pc=0.8,
                 pm=0.2,
                 seed=None):

        super().__init__(problem, seed)

        self.pop_size = pop_size
        self.iterations = iterations
        self.pc = pc
        self.pm = pm
        self.dim = self.problem.distance_matrix.shape[0]

    def _init_population(self):
        pop = []
        for _ in range(self.pop_size):
            tour = list(range(1, self.dim + 1))
            np.random.shuffle(tour)
            pop.append(tour)
        return pop

    def _mutate(self, tour):
        i, j = np.random.choice(self.dim, 2, replace=False)
        tour[i], tour[j] = tour[j], tour[i]
        return tour

    def run(self):

        self._start_timer()

        population = self._init_population()

        for _ in range(self.iterations):

            new_population = []

            for i in range(self.pop_size):

                left = population[i - 1]
                center = population[i]
                right = population[(i + 1) % self.pop_size]

                candidates = [left, center, right]
                distances = [
                    self.problem.calculate_tour_length(ind)
                    for ind in candidates
                ]

                best = candidates[np.argmin(distances)].copy()

                if np.random.rand() < self.pm:
                    best = self._mutate(best)

                new_population.append(best)

                dist = self.problem.calculate_tour_length(best)

                if dist < self.best_distance:
                    self.best_distance = dist
                    self.best_tour = best.copy()

            population = new_population
            self.history.append(self.best_distance)

        self._stop_timer()
        return self