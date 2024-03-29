import math

class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.qubit_states = {}  # To keep track of qubit states, if needed

    def analyze(self):
        from parser import SetStatement, MeasurementStatement
        for statement in self.ast:
            if isinstance(statement, SetStatement):
                self.check_qubit_normalization(statement)

    def check_qubit_normalization(self, statement):
        # Assuming complex_number1 and complex_number2 are strings in the format '1+0i'
        state0 = complex(statement.complex_number1.replace('i', 'j'))  # Convert to Python complex format
        state1 = complex(statement.complex_number2.replace('i', 'j'))

        state0_real = state0.real
        state0_imag = state0.imag
        state1_real = state1.real
        state1_imag = state1.imag

        print(f"Checking normalization for qubit {statement.qubit_id}:")
        print(f"State 0: Real {state0_real}, Imag {state0_imag}")
        print(f"State 1: Real {state1_real}, Imag {state1_imag}")

        norm = state0_real**2 + state0_imag**2 + state1_real**2 + state1_imag**2
        print(f"Calculated norm for qubit {statement.qubit_id}: {norm}")

        if not math.isclose(norm, 1.0, rel_tol=1e-9):
            error_msg = f"Qubit {statement.qubit_id} normalization error: |α|^2 + |β|^2 = {norm} ≠ 1"
            print(error_msg)
            raise ValueError(error_msg)

    def check_measurement(self, statement):
        # Here you might want to check that the qubit exists and is initialized
        # For example:
        if statement.qubit_id not in self.qubit_states:
            raise ValueError(f"Qubit {statement.qubit_id} has not been initialized.")
        print(f"Qubit {statement.qubit_id} is ready for measurement.")
        # You might also set or change the state here based on your simulation's requirements
