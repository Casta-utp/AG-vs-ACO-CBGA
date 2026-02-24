import itertools
import pandas as pd


class GridSearch:

    def __init__(self, algorithm_class, param_grid, seeds):
        self.algorithm_class = algorithm_class
        self.param_grid = param_grid
        self.seeds = seeds

    def run(self, problem):

        keys = self.param_grid.keys()
        combinations = list(itertools.product(*self.param_grid.values()))

        results = []

        for combo in combinations:
            params = dict(zip(keys, combo))

            distances = []

            for seed in self.seeds:
                algo = self.algorithm_class(
                    problem,
                    seed=seed,
                    **params
                ).run()

                distances.append(algo.best_distance)

            results.append({
                **params,
                "Mean Distance": sum(distances) / len(distances)
            })

        return pd.DataFrame(results)