# QML-BENCHMARK-HARNESS

A Python project to benchmark simple quantum-inspired variational workflows.

This repository provides lightweight utilities to construct variational circuits, run a VQE-style workflow (not a full VQE implementation), and collect benchmark metrics across different problem sizes.

Key components
- `circuits/variational_circuit.py`: helpers to build a parameterised circuit.
- `workflows/vqe_workflow.py`: a VQE-style workflow that prepares a circuit, runs a backend, and returns simple metrics (depth, runtime, unique outcomes). This is a simplified, illustrative workflow — it is not a production VQE implementation.
- `benchmarking/benchmark_runner.py`: runs the workflow over a list of qubit counts and saves results to `results/benchmark_results.csv`.
- `benchmarking/benchmark_runner.py::save_results()`: helper to persist benchmark DataFrame to CSV (creates directories as needed).

Getting started

1. Create and activate a Python environment (recommended)

- Create the virtual environment:

```bash
python -m venv .venv
```

- Activate the environment:

- PowerShell (Windows):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Command Prompt (Windows):

```cmd
.\.venv\Scripts\activate.bat
```

- macOS / Linux:

```bash
source .venv/bin/activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the example benchmark (writes to `results/benchmark_results.csv`):

```bash
python main.py
```

Testing

- Run tests (simple, cross-platform):

```bash
pytest -q
```

- If you encounter import errors when running tests (rare), run with the project root on `PYTHONPATH`:

- PowerShell:

```powershell
$env:PYTHONPATH = '.'; pytest -q
```

- macOS / Linux:

```bash
PYTHONPATH='.' pytest -q
```

## VQE-style workflow (note: illustrative only)

The workflow implemented in `workflows/vqe_workflow.py` follows the high-level structure of a Variational Quantum Eigensolver (VQE) experiment but is intentionally simplified for benchmarking and demonstration:

- Prepare a parameterised variational circuit depending on `num_qubits` and optional parameters.
- Optionally transpile or adapt the circuit for a chosen backend (tests monkeypatch `transpile` to a no-op).
- Execute the circuit on a backend (simulated or stubbed) for a number of `shots` and collect measurement outcomes.
- Compute and return simple metrics:
	- `num_qubits`: the problem size used
	- `depth`: circuit depth (an indicator of circuit complexity)
	- `runtime_sec`: measured runtime for execution (wall time)
	- `shots`: number of measurement shots used
	- `unique_outcomes`: count of unique measurement results observed

Because the project is intended for benchmarking, the focus is on producing repeatable, comparable metrics rather than on energy minimisation or optimisation loops typically present in a full VQE implementation.

## Contributing

Contributions are welcome. Please open issues or pull requests for feature requests, bug fixes, or enhancements.
