from core.problem import TSPProblem
from core.runner import ExperimentRunner
from algorithms.classic_ga import ClassicGA
from algorithms.aco import ACO
from algorithms.cbga import CBGA
from algorithms.random_search import RandomSearch
from tuning.grid_search import GridSearch
from visualization.plotter import Plotter
from config import KNOWN_OPTIMA, TSP_INSTANCES


SEEDS = [42, 43, 44, 45, 46]


# ==============================
# UTILIDADES
# ==============================

def pause():
    input("\nPresione ENTER para volver al menú...")


def select_algorithm():

    print("\n=== SELECCIÓN DE ALGORITMO ===")
    print("1. Genetic Algorithm (GA)")
    print("2. Ant Colony Optimization (ACO)")
    print("3. Cellular GA (CBGA)")
    print("4. Random Search")
    print("5. Volver")

    choice = input("Seleccione opción: ")

    mapping = {
        "1": ClassicGA,
        "2": ACO,
        "3": CBGA,
        "4": RandomSearch
    }

    if choice == "5":
        return None

    return mapping.get(choice, None)


def select_city():

    print("\n=== SELECCIÓN DE CIUDAD ===")
    cities = list(TSP_INSTANCES.keys())

    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")

    print(f"{len(cities)+1}. Comparar TODAS")
    print(f"{len(cities)+2}. Volver")

    try:
        choice = int(input("Seleccione opción: "))
    except:
        return None

    if choice == len(cities) + 2:
        return None

    if choice == len(cities) + 1:
        return "ALL"

    if 1 <= choice <= len(cities):
        return cities[choice - 1]

    return None


def ask_visualization():
    choice = input("¿Desea visualizar resultados? (s/n): ")
    return choice.lower() == "s"


# ==============================
# EJECUCIÓN EXPERIMENTO
# ==============================

def get_default_params(algorithm_class):

    if algorithm_class == ClassicGA:
        return dict(pop_size=100, iterations=500, pc=0.85, pm=0.15)

    elif algorithm_class == ACO:
        return dict(num_ants=30, iterations=300, alpha=1, beta=5, rho=0.5)

    elif algorithm_class == CBGA:
        return dict(pop_size=100, iterations=500, pc=0.8, pm=0.2)

    elif algorithm_class == RandomSearch:
        return dict(iterations=1000)

    return {}


def run_experiment(algorithm_class, city, visualize):

    problem = TSPProblem(city)

    runner = ExperimentRunner(
        algorithm_class=algorithm_class,
        seeds=SEEDS,
        known_optimum=KNOWN_OPTIMA.get(city)
    )

    params = get_default_params(algorithm_class)

    df = runner.run(problem, **params)

    if visualize:
        print("\nGenerando visualizaciones...")

        # 📊 Boxplot con 5 semillas
        Plotter.plot_boxplot(df, f"Boxplot - {city}")

        # 📈 Convergencia promedio + desviación estándar
        Plotter.plot_convergence(df)

        # 🏆 Obtener mejor semilla real
        best_row = df.loc[df["Best Distance"].idxmin()]
        best_seed = int(best_row["Seed"])

        # Re-ejecutar esa semilla para obtener la mejor ruta
        best_algo = algorithm_class(problem, seed=best_seed, **params).run()

        Plotter.plot_tour(problem, best_algo.best_tour, f"Mejor Ruta - {city}")

def run_comparison(algorithm_class):

    print("\n=== COMPARACIÓN EN TODAS LAS CIUDADES ===")

    for city in TSP_INSTANCES.keys():
        print(f"\n--- {city} ---")
        run_experiment(algorithm_class, city, visualize=False)


def run_tuning(algorithm_class):

    print("\n=== GRID SEARCH ===")

    city = select_city()

    if city is None or city == "ALL":
        print("Debe seleccionar una ciudad válida.")
        return

    problem = TSPProblem(city)

    if algorithm_class == ClassicGA:
        param_grid = {
            "pop_size": [80, 100],
            "pc": [0.7, 0.85],
            "pm": [0.1, 0.2],
            "iterations": [300]
        }

    elif algorithm_class == ACO:
        param_grid = {
            "num_ants": [20, 30],
            "alpha": [1, 2],
            "beta": [3, 5],
            "iterations": [200]
        }

    elif algorithm_class == CBGA:
        param_grid = {
            "pop_size": [80, 100],
            "pm": [0.1, 0.2],
            "iterations": [300]
        }

    else:
        param_grid = {
            "iterations": [500, 1000]
        }

    gs = GridSearch(algorithm_class, param_grid, SEEDS)

    df = gs.run(problem)

    print("\nResultados Grid Search:")
    print(df.sort_values("Mean Distance"))


# ==============================
# MENÚ PRINCIPAL EN BUCLE
# ==============================

def main_menu():

    while True:

        print("\n====================================")
        print("   TSP METAHEURÍSTICAS - MENÚ")
        print("====================================")
        print("1. Ejecutar algoritmo")
        print("2. Tuning (Grid Search)")
        print("3. Salir")

        main_choice = input("Seleccione opción: ")

        if main_choice == "1":

            algorithm_class = select_algorithm()

            if algorithm_class is None:
                continue

            city = select_city()

            if city is None:
                continue

            if city == "ALL":
                run_comparison(algorithm_class)
            else:
                visualize = ask_visualization()
                run_experiment(algorithm_class, city, visualize)

            pause()

        elif main_choice == "2":

            algorithm_class = select_algorithm()

            if algorithm_class is None:
                continue

            run_tuning(algorithm_class)
            pause()

        elif main_choice == "3":
            print("\nSaliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main_menu()