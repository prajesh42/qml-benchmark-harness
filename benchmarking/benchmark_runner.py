from pathlib import Path
import pandas as pd
from workflows.vqe_workflow import run_vqe

def save_results(df: pd.DataFrame, filepath: str):
    path = Path(filepath)

    # Create parent directory if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

def run_benchmark(qubit_list):
    results = []

    for qubits in qubit_list:
        print(f"Running benchmark for {qubits} qubits...")
        metrics = run_vqe(qubits)
        results.append(metrics)

    df = pd.DataFrame(results)
    save_results(df, "results/benchmark_results.csv")
    return df