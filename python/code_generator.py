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
        # Import qubit handling
        from c_integration import Qubit
        # Convert the state strings to real and imaginary parts as needed
        state0_real = float(statement.state0.strip('{}').split()[0])  # Extract real part
        state0_imag = float(statement.state0.strip('{}').split()[1]) if len(statement.state0.strip('{}').split()) > 1 else 0.0  # Extract imaginary part if present
        state1_real = float(statement.state1.strip('{}').split()[0])  # Extract real part
        state1_imag = float(statement.state1.strip('{}').split()[1]) if len(statement.state1.strip('{}').split()) > 1 else 0.0  # Extract imaginary part if present

        # Create a Qubit instance
        qubit = Qubit(state0_real=state0_real, state0_imag=state0_imag,
                      state1_real=state1_real, state1_imag=state1_imag)

        # Call the initialize_qubit method of QuantumLib with the qubit instance
        self.lib.initialize_qubit(ctypes.byref(qubit), state0_real, state0_imag, state1_real, state1_imag)

        # Add to code (if you're generating a representation, or directly execute the function call)
        # Assuming you're keeping track of generated code or direct execution
        #self.code.append(f"Initialized qubit with states {statement.state0} and {statement.state1}")

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

