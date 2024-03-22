import re

# Define a regular expression for each token
TOKEN_REGEX = [
    (r'[ \t]+', None),  # Ignore spaces and tabs
    (r'apply', 'APPLY'),
    (r'to', 'TO'),
    (r'qubit', 'QUBIT'),
    (r'X|H|CNOT', 'GATE'),
    (r'\d+', 'NUMBER'),
    (r';', 'SEMICOLON'),
    (r'\n', 'NEWLINE'),
    (r'.', 'UNKNOWN'),  # Any other character
]

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

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
                if token_type:  # If not None (ignoring spaces/tabs)
                    tokens.append(Token(token_type, match))
                break
        if not match:
            raise SyntaxError(f'Illegal character: {code[0]}')
        code = code[len(match):]
    return tokens

# Example usage
code = """
apply X to qubit 0;
apply H to qubit 1;
"""
tokens = lexer(code)
for token in tokens:
    print(token)

