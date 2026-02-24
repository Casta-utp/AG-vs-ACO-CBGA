import numpy as np
from core.base_algorithm import TSPAlgorithm


class RandomSearch(TSPAlgorithm):

    def __init__(self, problem, iterations=1000, seed=None):
        super().__init__(problem, seed)
        self.iterations = iterations

    def run(self):
        self._start_timer()

        dim = self.problem.distance_matrix.shape[0]

        for _ in range(self.iterations):
            tour = list(range(1, dim + 1))
            np.random.shuffle(tour)

            dist = self.problem.calculate_tour_length(tour)

            if dist < self.best_distance:
                self.best_distance = dist
                self.best_tour = tour.copy()

            self.history.append(self.best_distance)

        self._stop_timer()
        return self