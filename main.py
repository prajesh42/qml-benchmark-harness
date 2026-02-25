from benchmarking.benchmark_runner import run_benchmark

if __name__ == "__main__":
    qubit_list = [2, 4, 6, 8]
    df = run_benchmark(qubit_list)
    print(df)