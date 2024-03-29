import ctypes
from parser import SetStatement, GateApplication
from c_integration import Qubit

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.lib = ctypes.CDLL('./lib/libquantum.so')
        self.lib.initialize_qubit.argtypes = [ctypes.POINTER(Qubit), ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
        self.lib.initialize_qubit.restype = None

    def generate(self):
        for statement in self.ast:
            if isinstance(statement, SetStatement):
                self.handle_set_statement(statement)
            elif isinstance(statement, GateApplication):
                self.handle_gate_application(statement)
        return "\n".join(self.code)

    def handle_set_statement(self, statement):
        state0_real, state0_imag = self.parse_complex_number(statement.complex_number1)
        state1_real, state1_imag = self.parse_complex_number(statement.complex_number2)

        print(f"Debug: state0_real={state0_real}, state0_imag={state0_imag}, state1_real={state1_real}, state1_imag={state1_imag}")

        qubit = Qubit(state0_real=state0_real, state0_imag=state0_imag, state1_real=state1_real, state1_imag=state1_imag)

        self.lib.initialize_qubit(ctypes.byref(qubit), state0_real, state0_imag, state1_real, state1_imag)

    def handle_gate_application(self, statement):
        qubit_number = ctypes.c_int(int(statement.qubit_number))
        apply_gate_func = getattr(self.lib, f"apply_{statement.gate.lower()}_gate")
        apply_gate_func(qubit_number)

    def parse_complex_number(self, complex_str):
        parts = complex_str.strip('{}').split('+')
        real_part = float(parts[0]) if parts else 0.0
        imag_part = float(parts[1].replace('i', '')) if len(parts) > 1 else 0.0
        return real_part, imag_part

