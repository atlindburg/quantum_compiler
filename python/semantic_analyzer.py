import math
class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast

    def analyze(self):
        from parser import SetStatement
        for statement in self.ast:
            if isinstance(statement, SetStatement):
                self.check_qubit_normalization(statement)

    def check_qubit_normalization(self, statement):
        # Assuming state0 and state1 are the amplitude values of the qubit
        print(f"Checking normalization for qubit {statement.qubit_id} with states {statement.state0} and {statement.state1}.")
        state0 = float(statement.state0.strip('{}'))
        state1 = float(statement.state1.strip('{}'))
        # Calculate the norm
        norm = state0 ** 2 + state1 ** 2
        print(f"Calculated norm for qubit {statement.qubit_id}: {norm}")

        # Check if the norm is close to 1 within some tolerance
        if not math.isclose(norm, 1.0, rel_tol=1e-9):
            if not math.isclose(norm, 1.0, rel_tol=1e-9):
                print(f"Qubit {statement.qubit_id} normalization error: |α|^2 + |β|^2 = {norm} ≠ 1")
                raise SemanticError(f"Qubit {statement.qubit_id} is not properly normalized: |α|^2 + |β|^2 = {norm} ≠ 1")

