from parser import SetStatement, GateApplication
class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []

    def generate(self):
        for statement in self.ast:
            if isinstance(statement, SetStatement):
                self.handle_set_statement(statement)
            elif isinstance(statement, GateApplication):
                self.handle_gate_application(statement)
        return "\n".join(self.code)

    def handle_set_statement(self, statement):
        c_code = f"initialize_qubit({statement.qubit_id}, {statement.state0}, {statement.state1});"
        self.code.append(c_code)

    def handle_gate_application(self, statement):
        c_code = f"apply_{statement.gate.lower()}_gate({statement.qubit_number});"
        self.code.append(c_code)

# Example usage:
# generator = CodeGenerator(ast)
# generated_code = generator.generate()
# print(generated_code)

