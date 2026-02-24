import time
import numpy as np


class TSPAlgorithm:

    def __init__(self, problem, seed=None):
        self.problem = problem
        self.seed = seed
        self.best_tour = None
        self.best_distance = float("inf")
        self.history = []
        self.exec_time = 0

        if seed is not None:
            np.random.seed(seed)

    def run(self):
        raise NotImplementedError("Debes implementar run()")

    def _start_timer(self):
        self._start = time.time()

    def _stop_timer(self):
        self.exec_time = time.time() - self._start