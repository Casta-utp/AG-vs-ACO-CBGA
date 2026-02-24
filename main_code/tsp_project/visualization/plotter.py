import matplotlib.pyplot as plt
import numpy as np


class Plotter:

    @staticmethod
    def plot_convergence(df_results):

        if "Historial" not in df_results.columns:
            print("No se encontró la columna 'Historial'")
            return

        histories = df_results["Historial"].tolist()

        if len(histories) == 0:
            print("No hay historiales para graficar.")
            return

        # Asegurar misma longitud
        min_len = min(len(h) for h in histories)
        histories = [h[:min_len] for h in histories]

        histories_array = np.array(histories)

        mean_history = np.mean(histories_array, axis=0)
        std_history = np.std(histories_array, axis=0)

        plt.figure(figsize=(10, 6))
        plt.plot(mean_history, label="Promedio")
        plt.fill_between(
            range(min_len),
            mean_history - std_history,
            mean_history + std_history,
            alpha=0.3,
            label="Desviación Estándar"
        )

        plt.title("Curva de Convergencia Promedio")
        plt.xlabel("Iteraciones")
        plt.ylabel("Mejor Distancia Encontrada")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_boxplot(results_df, title="Boxplot Comparison"):

        if "Best Distance" not in results_df.columns:
            print("El DataFrame no contiene 'Best Distance'")
            return

        values = results_df["Best Distance"].values

        if len(values) == 0:
            print("No hay datos para boxplot.")
            return

        plt.figure(figsize=(6, 5))
        plt.boxplot(values)
        plt.ylabel("Best Distance")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_tour(problem, tour, title="Best Tour"):

        if tour is None:
            print("No hay ruta para graficar.")
            return

        if not hasattr(problem.problem, "node_coords"):
            print("No hay coordenadas disponibles para graficar.")
            return

        coords = np.array([
            problem.problem.node_coords[i]
            for i in sorted(problem.problem.node_coords.keys())
        ])

        tour = [i - 1 for i in tour]
        tour.append(tour[0])

        plt.figure(figsize=(6, 6))
        plt.plot(coords[tour, 0], coords[tour, 1], marker='o')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.show()