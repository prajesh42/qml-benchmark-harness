from circuits.variational_circuit import create_variational_circuit
import numpy as np

def test_create_variational_circuit():
    num_qubits = 3
    parameters = [0.5, 1.0, 1.5]
    
    circuit = create_variational_circuit(num_qubits, parameters)
    
    # Check if the circuit has the correct number of qubits
    assert circuit.num_qubits == num_qubits
    
    # Check if the circuit has the correct number of gates (3 RY gates + 2 CNOT gates)
    expected_num_gates = num_qubits + (num_qubits - 1)  # RY gates + CNOT gates
    assert len(circuit.data) == expected_num_gates
    
    # Check if the first gate is an RY gate with the correct parameter
    first_gate = circuit.data[0]
    assert first_gate.operation.name == 'ry'
    assert np.isclose(first_gate.operation.params[0], parameters[0])