import numpy as np
from core.base_algorithm import TSPAlgorithm


class ACO(TSPAlgorithm):

    def __init__(self, problem,
                 num_ants=30,
                 iterations=300,
                 alpha=1,
                 beta=5,
                 rho=0.5,
                 q=100,
                 seed=None):

        super().__init__(problem, seed)

        self.num_ants = num_ants
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q

        self.dist = self.problem.distance_matrix
        self.dim = self.dist.shape[0]

        self.pheromone = np.ones((self.dim, self.dim))
        self.heuristic = 1 / (self.dist + 1e-10)

    def _construct_solution(self):

        solutions = []

        for _ in range(self.num_ants):
            tour = [np.random.randint(self.dim)]
            unvisited = set(range(self.dim)) - set(tour)

            while unvisited:
                current = tour[-1]
                probs = []

                for j in unvisited:
                    tau = self.pheromone[current][j] ** self.alpha
                    eta = self.heuristic[current][j] ** self.beta
                    probs.append(tau * eta)

                probs = np.array(probs)
                probs = probs / probs.sum()

                next_city = np.random.choice(list(unvisited), p=probs)
                tour.append(next_city)
                unvisited.remove(next_city)

            solutions.append([c + 1 for c in tour])

        return solutions

    def _update_pheromone(self, solutions):

        self.pheromone *= (1 - self.rho)

        for tour in solutions:
            dist = self.problem.calculate_tour_length(tour)
            for i in range(len(tour)):
                a = tour[i] - 1
                b = tour[(i + 1) % len(tour)] - 1
                self.pheromone[a][b] += self.q / dist

    def run(self):

        self._start_timer()

        for _ in range(self.iterations):

            solutions = self._construct_solution()

            for tour in solutions:
                dist = self.problem.calculate_tour_length(tour)

                if dist < self.best_distance:
                    self.best_distance = dist
                    self.best_tour = tour.copy()

            self.history.append(self.best_distance)
            self._update_pheromone(solutions)

        self._stop_timer()
        return self