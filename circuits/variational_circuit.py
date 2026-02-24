from qiskit import QuantumCircuit
import numpy as np

def create_variational_circuit(num_qubits: int, parameters: np.ndarray) -> QuantumCircuit:
    """
    Creates a variational quantum circuit with the given parameters.

    Args:
        num_qubits (int): The number of qubits in the circuit.
        parameters (np.ndarray): An array of parameters for the gates.

    Returns:
        QuantumCircuit: The created variational quantum circuit.
    """
    circuit = QuantumCircuit(num_qubits)

    # Apply parameterized RY gates to each qubit
    for i in range(num_qubits):
        circuit.ry(parameters[i], i)

    # Add entangling gates (CNOTs) between adjacent qubits
    for i in range(num_qubits - 1):
        circuit.cx(i, i + 1)

    return circuit