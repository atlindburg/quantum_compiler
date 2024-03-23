import re

# Define a regular expression for each token
TOKEN_REGEX = [
    (r'[ \t]+', None),  # Ignore spaces and tabs
    (r'\n', 'NEWLINE'),
    (r'apply', 'APPLY'),
    (r'TO', 'TO'),
    (r'qubit', 'QUBIT'),
    (r'X|H|CNOT', 'GATE'),
    (r'\d+', 'NUMBER'),
    (r';', 'SEMICOLON'),
    (r'SET', 'SET'),  # Added token for SET
    (r'q[0-9]+', 'QUBIT_ID'),  # Pattern for qubit identifiers like q1, q2, etc.
    (r'\{[01]\}', 'QUBIT_STATE'),  # Pattern for qubit state {0} or {1}
    (r'.', 'UNKNOWN'),  # Any other character
]

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

def lexer(code):
    tokens = []
    while code:
        match = None
        for regex, token_type in TOKEN_REGEX:
            regex_match = re.match(regex, code)
            if regex_match:
                match = regex_match.group(0)
                if token_type == 'UNKNOWN':
                    raise SyntaxError(f'Unknown token: {match}')
                elif token_type:  # If not None (ignoring spaces, tabs, and newlines)
                    tokens.append(Token(token_type, match))
                break
        code = code[len(match):]  # This line should be aligned with while loop
    return tokens

# Ensure this part is commented out or under a '__main__' guard
# code = "some code here"
# tokens = lexer(code)
# for token in tokens:
#     print(token)

# Or correctly placed under a '__main__' guard

# Example usage
#code = """
#apply X to qubit 0;
#apply H to qubit 1;
"""
#tokens = lexer(code)
#for token in tokens:
   # print(token)
"""
