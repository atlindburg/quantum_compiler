class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def eat(self, token_type):
        print(f"Trying to eat: {token_type}, current token: {self.current_token().type}")
        if self.current_token().type == token_type:
            self.current_token_index += 1
        else:
            raise SyntaxError(f"Expected token {token_type}, got {self.current_token().type}")

    def current_token(self):
        return self.tokens[self.current_token_index]

    def parse(self):
        statements = []
        while self.current_token().type != 'EOF':
            if self.current_token().type == 'NEWLINE':  # Skip over any NEWLINE tokens
                self.eat('NEWLINE')
                continue  # Move to the next token without executing the rest of the loop
            elif self.current_token().type == 'SET':
                statements.append(self.parse_set_statement())
            elif self.current_token().type == 'APPLY':
                statements.append(self.parse_gate_application())
            else:
                raise SyntaxError(f"Unknown statement start with token: {self.current_token().type} {self.current_token().value}")
        return statements

    def parse_set_statement(self):
        self.eat('SET')
        qubit_id = self.current_token().value
        self.eat('QUBIT_ID')
        self.eat('TO')

        # Handling both real, imaginary and complex numbers
        if self.current_token().type == 'COMPLEX_NUMBER':
            complex_number = self.current_token().value
            self.eat('COMPLEX_NUMBER')
        else:
            complex_number = None  # or use a default value or an error handling
            raise SyntaxError("Expected a complex or real number for qubit amplitude")

        state0 = self.current_token().value
        self.eat('QUBIT_STATE')

        if self.current_token().type == 'COMPLEX_NUMBER':
            complex_number2 = self.current_token().value
            self.eat('COMPLEX_NUMBER')
        else:
            complex_number2 = None  # or use a default value or an error handling
            raise SyntaxError("Expected a complex or real number for qubit amplitude")

        state1 = self.current_token().value
        self.eat('QUBIT_STATE')

        self.eat('SEMICOLON')

        return SetStatement(qubit_id, complex_number, state0, complex_number2, state1)

    def parse_gate_application(self):

        self.eat('APPLY')
        gate = self.current_token().value
        self.eat('GATE')
        self.eat('TO')
        self.eat('QUBIT')
        qubit_number = self.current_token().value
        self.eat('NUMBER')
        self.eat('SEMICOLON')
        return GateApplication(gate, qubit_number)

# Define AST node classes here, e.g.,
class SetStatement:
    def __init__(self, qubit_id, complex_number1, state0, complex_number2, state1):
        self.qubit_id = qubit_id
        self.complex_number1 = complex_number1  # Changed from number1 to complex_number1
        self.state0 = state0
        self.complex_number2 = complex_number2  # Changed from number2 to complex_number2
        self.state1 = state1

        # Debugging print statement
        print(f"Initializing SetStatement with:")
        print(f"qubit_id: {qubit_id}, complex_number1: {complex_number1}, state0: {state0}, complex_number2: {complex_number2}, state1: {state1}")


class GateApplication:
    def __init__(self, gate, qubit_number):
        self.gate = gate
        self.qubit_number = qubit_number

# Extend the lexer to emit an 'EOF' token at the end of the input

