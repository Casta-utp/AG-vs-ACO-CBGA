import pandas as pd
import numpy as np


class ExperimentRunner:

    def __init__(self, algorithm_class, seeds, known_optimum=None):
        self.algorithm_class = algorithm_class
        self.seeds = seeds
        self.known_optimum = known_optimum

    def _calculate_gap(self, value):
        if self.known_optimum is None:
            return np.nan
        return ((value - self.known_optimum) /
                self.known_optimum) * 100

    def _print_statistics(self, df):

        algo_name = self.algorithm_class.__name__

        mean_distance = df["Best Distance"].mean()
        std_distance = df["Best Distance"].std()
        best_distance = df["Best Distance"].min()
        worst_distance = df["Best Distance"].max()
        mean_time = df["Time"].mean()
        mean_gap = df["GAP (%)"].mean()

        print("\n========================================")
        print(f'Resultados para "{algo_name}"')
        print("========================================")
        print(f"Distancia Promedio: {mean_distance:.4f} ± {std_distance:.4f}")
        print(f"Mejor Distancia Global: {best_distance:.4f}")
        print(f"Peor Distancia Global: {worst_distance:.4f}")
        print(f"Tiempo Promedio: {mean_time:.4f} segundos")

        if not np.isnan(mean_gap):
            print(f"GAP Promedio: {mean_gap:.4f} %")

        print("========================================\n")

    def run(self, problem, **kwargs):

        results = []

        for seed in self.seeds:
            algo = self.algorithm_class(
                problem,
                seed=seed,
                **kwargs
            ).run()

            results.append({
                "Seed": seed,
                "Best Distance": algo.best_distance,
                "Time": algo.exec_time,
                "GAP (%)": self._calculate_gap(algo.best_distance),
                "Historial": algo.history   # 🔥 CLAVE
            })

        df = pd.DataFrame(results)

        print("\nResultados por semilla:")
        print(df[["Seed", "Best Distance", "Time", "GAP (%)"]])

        self._print_statistics(df)

        return df