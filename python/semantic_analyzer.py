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
        # Parsing the complex numbers represented in state0 and state1
        state0_real, state0_imag = self.parse_complex_number(statement.state0)
        state1_real, state1_imag = self.parse_complex_number(statement.state1)

        print(f"Checking normalization for qubit {statement.qubit_id}:")
        print(f"State 0: Real {state0_real}, Imag {state0_imag}")
        print(f"State 1: Real {state1_real}, Imag {state1_imag}")

        # Calculate the norm considering potential imaginary parts
        norm = (state0_real ** 2 + state0_imag ** 2) + (state1_real ** 2 + state1_imag ** 2)
        print(f"Calculated norm for qubit {statement.qubit_id}: {norm}")

        if not math.isclose(norm, 1.0, rel_tol=1e-9):
            error_msg = f"Qubit {statement.qubit_id} normalization error: |α|^2 + |β|^2 = {norm} ≠ 1"
            print(error_msg)
            raise ValueError(error_msg)

    def parse_complex_number(self, complex_str):
        """
        Parses a string representing a complex number in the format '{real} {imag}'
        and returns the real and imaginary parts as floats. Defaults to 0 for the imaginary part if not provided.
        """
        parts = complex_str.strip('{}').split()
        real_part = float(parts[0]) if parts else 0.0
        imag_part = float(parts[1]) if len(parts) > 1 else 0.0
        return real_part, imag_part

