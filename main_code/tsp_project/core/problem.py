import tsplib95
import numpy as np
import os
from config import TSP_INSTANCES


class TSPProblem:

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.problem = self._load_problem()
        self.distance_matrix = self._get_distance_matrix()

    def _load_problem(self):
        path = TSP_INSTANCES.get(self.instance_name)
        if not path or not os.path.exists(path):
            raise FileNotFoundError(f"No se encontró {self.instance_name}")
        return tsplib95.load(path)

    def _get_distance_matrix(self):
        problem = self.problem

        if problem.is_explicit():
            nodes = list(problem.get_nodes())
            dim = len(nodes)
            matrix = np.zeros((dim, dim))
            for i in range(dim):
                for j in range(dim):
                    matrix[i, j] = problem.get_weight(nodes[i], nodes[j])
            return matrix

        elif problem.is_full_matrix():
            return np.array(problem.edge_weights)

        else:
            coords = np.array([
                problem.node_coords[i]
                for i in sorted(problem.node_coords.keys())
            ])
            return np.linalg.norm(
                coords[:, np.newaxis, :] - coords[np.newaxis, :, :],
                axis=2
            )

    def calculate_tour_length(self, tour):
        total = 0
        n = len(tour)
        for i in range(n):
            a = tour[i] - 1
            b = tour[(i + 1) % n] - 1
            total += self.distance_matrix[a, b]
        return total