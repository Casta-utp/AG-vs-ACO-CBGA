# 🧬 AG-vs-ACO-CBGA  
**Comparison and Hyperparameter Tuning of GA, ACO, and Chu–Beasley GA (CBGA) for TSPLIB TSP Instances**

> Modular OOP implementation with multi-seed statistical evaluation and convergence analysis.

---

## 🚀 Workshop Overview  
### Comparison and Tuning of GA vs ACO for the TSP (TSPLIB)  
### 🔥 PLUS Extension: Chu–Beasley Genetic Algorithm (CBGA)

This project presents a modular, object-oriented implementation of metaheuristic algorithms for solving the **Traveling Salesman Problem (TSP)** using benchmark instances from **TSPLIB**.

---

## 🧠 Algorithms Implemented

The study includes the following metaheuristics:

- **Genetic Algorithm (GA)**
- **Ant Colony Optimization (ACO)**
- **Chu–Beasley Genetic Algorithm (CBGA)**
- **Random Search** *(baseline reference)*

---

## 🔬 Research Objectives

- Compare the performance of GA and ACO on multiple TSPLIB instances  
- Extend the comparison by incorporating the Chu–Beasley GA (CBGA)  
- Perform hyperparameter tuning using Grid Search  
- Evaluate robustness through multi-seed statistical analysis  
- Analyze convergence behavior and variability across runs  

---

## 📊 Experimental Methodology

### 🔁 Multi-Seed Evaluation  
Each experiment is executed with **5 independent runs (seeds 42–46)** to ensure statistical robustness.

### 📈 Reported Metrics

The following statistical indicators are computed:

- **Mean ± Standard Deviation**
- **Best Global Distance**
- **Worst Global Distance**
- **Average Execution Time**
- **Mean GAP (%)** relative to known optimal solutions
- **Convergence Curves (mean ± std)**
- **Boxplot Distribution Analysis**
- **Best Tour Visualization**

---

## 🏗️ System Architecture

The project follows a clean **Object-Oriented Programming (OOP)** modular structure:

```bash
tsp_project/
│
├── core/              # Problem abstraction and experiment runner
├── algorithms/        # GA, ACO, CBGA, Random Search
├── tuning/            # Grid Search module
├── visualization/     # Convergence and statistical plots
├── config.py          # Instances and known optima
└── main.py            # Interactive execution menu
```


### Architectural Principles

- Separation of concerns  
- Algorithm abstraction via base class  
- Reproducible experimental framework  
- Extensibility for future metaheuristics  

---

## ⚙️ Key Features

- Fully modular OOP design  
- Multi-instance evaluation (TSPLIB)  
- Automated statistical reporting  
- Convergence curve visualization (mean ± std)  
- Hyperparameter tuning via Grid Search  
- Robust multi-seed experimentation  
- Interactive execution menu  

---

## 🎯 Academic Focus

This project emphasizes proper experimental methodology in stochastic metaheuristics, including:

- Statistical validation  
- Robustness analysis  
- Performance comparison  
- Reproducibility of results  

The implementation aims to follow good research practices for computational experimentation in metaheuristic optimization.

---

## 📎 Additional Materials

The repository includes complementary academic material:

- 📄 **Technical Report** containing detailed experimental results and statistical analysis  
- 📓 **Google Colab Notebook** for easy execution and reproducibility  
- 📊 **Brief Presentation** summarizing methodology, comparison, and key findings  

These materials provide a complete overview of the experimental framework, results interpretation, and conclusions derived from the comparative study.
