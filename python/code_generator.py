import ctypes
from parser import SetStatement, GateApplication

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        # Load the shared library
        self.lib = ctypes.CDLL('./lib/libquantum.so')  # Adjust the path as necessary

    def generate(self):
        for statement in self.ast:
            if isinstance(statement, SetStatement):
                self.handle_set_statement(statement)
            elif isinstance(statement, GateApplication):
                self.handle_gate_application(statement)
        return "\n".join(self.code)

    def handle_set_statement(self, statement):
        # Prepare the arguments as ctypes
        qubit_id = ctypes.c_int(int(statement.qubit_id.strip('q')))  # Assuming qubit_id is like 'q1', 'q2', etc.
        state0 = ctypes.c_double(float(statement.state0.strip('{}')))  # Assuming state0 is like '{0.0}', '{1.0}', etc.
        state1 = ctypes.c_double(float(statement.state1.strip('{}')))
        # Call the C function
        self.lib.initialize_qubit(qubit_id, state0, state1)

    def handle_gate_application(self, statement):
        # Prepare the arguments as ctypes
        qubit_number = ctypes.c_int(int(statement.qubit_number))
        # Dynamically get the C function based on the gate type
        apply_gate_func = getattr(self.lib, f"apply_{statement.gate.lower()}_gate")
        # Call the C function
        apply_gate_func(qubit_number)

# Example usage:
# generator = CodeGenerator(ast)
# generated_code = generator.generate()
# print(generated_code)

