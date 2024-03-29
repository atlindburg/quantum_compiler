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
        # Now directly using the real and imaginary parts from the statement
        state0_real = float(statement.number1)
        state0_imag = float(statement.number1_imag)  # assuming number1_imag is the imaginary part of the first state
        state1_real = float(statement.number2)
        state1_imag = float(statement.number2_imag)  # assuming number2_imag is the imaginary part of the second state

        print(f"Checking normalization for qubit {statement.qubit_id}:")
        print(f"State 0: Real {state0_real}, Imag {state0_imag}")
        print(f"State 1: Real {state1_real}, Imag {state1_imag}")

        # Calculate the norm considering real and imaginary parts
        norm = state0_real**2 + state0_imag**2 + state1_real**2 + state1_imag**2
        print(f"Calculated norm for qubit {statement.qubit_id}: {norm}")

        # Check if the norm is close to 1 within some tolerance
        if not math.isclose(norm, 1.0, rel_tol=1e-9):
            error_msg = f"Qubit {statement.qubit_id} normalization error: |α|^2 + |β|^2 = {norm} ≠ 1"
            print(error_msg)
            raise ValueError(error_msg)

