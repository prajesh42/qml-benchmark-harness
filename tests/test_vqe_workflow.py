from workflows.vqe_workflow import run_vqe

class DummyResult:
    def get_counts(self):
        return {"00": 500, "11": 524}
    
class DummyJob:
    def result(self):
        return DummyResult()
    
class DummyBackend:
    def run(self, circuit, shots):
        return DummyJob()

def test_run_vqe_returns_expected_keys(monkeypatch):
    # Make transpile a no-op for unit testing
    import workflows.vqe_workflow as vw
    monkeypatch.setattr(vw, "transpile", lambda qc, backend: qc)

    metrics = run_vqe(num_qubits=2, seed=123, shots=1024, backend=DummyBackend())

    assert set(metrics.keys()) == {
        "num_qubits", "depth", "runtime_sec", "shots", "unique_outcomes"
    }
    assert metrics["num_qubits"] == 2
    assert metrics["shots"] == 1024
    assert metrics["unique_outcomes"] == 2
    assert metrics["depth"] > 0
    assert metrics["runtime_sec"] >= 0

def test_run_vqe_reproducible_depth(monkeypatch):
    import workflows.vqe_workflow as vw
    monkeypatch.setattr(vw, "transpile", lambda qc, backend: qc)

    metrics1 = run_vqe(num_qubits=4, seed=42, backend=DummyBackend())
    metrics2 = run_vqe(num_qubits=4, seed=42, backend=DummyBackend())

    assert metrics1["depth"] == metrics2["depth"]