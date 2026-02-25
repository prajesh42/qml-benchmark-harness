import numpy as np
import time
from qiskit_aer import Aer
from qiskit import transpile
from circuits.variational_circuit import create_variational_circuit

def run_vqe(num_qubits: int, seed: int = 42, shots: int = 1024, backend = None):
    """
    Runs a simple VQE workflow using a variational quantum circuit.

    Args:
        num_qubits (int): The number of qubits to use in the variational circuit.
        seed (int): Random seed for reproducibility. Default is 42.
        shots (int): Number of shots to execute the circuit. Default is 1024.
        backend: Optional backend to run the circuit on. If None, uses Aer simulator.

    Returns:
        dict: A dictionary containing the results of the VQE workflow.
    """
    # Initialize the Aer simulator backend
    if backend is None:
        backend = Aer.get_backend('aer_simulator')

    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate random parameters for the variational circuit
    parameters = np.random.rand(num_qubits)

    # Record the start time of the workflow
    start_time = time.time()

    # Create the variational quantum circuit
    circuit = create_variational_circuit(num_qubits, parameters)

    # Add measurement to all qubits
    circuit.measure_all()
    
    # Transpile the circuit for the backend
    transpiled_circuit = transpile(circuit, backend)

    # Run the circuit on the backend
    job = backend.run(transpiled_circuit, shots=shots)

    # Get the results from the job
    result = job.result()

    # Record the end time of the workflow
    end_time = time.time()

    # Get the counts of measurement outcomes
    counts = result.get_counts()

    return {
        "num_qubits": num_qubits,
        "depth": circuit.depth(),
        "runtime_sec": end_time - start_time,
        "shots": 1024,
        "unique_outcomes": len(counts),
    }