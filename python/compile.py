class Compile:
    def __init__(self, source_code):
        self.source_code = source_code

    def compile(self):
        print("Compiling the source code...")
        # Tokenize the source code using lexer
        from .lexer import lexer
        tokens = lexer(self.source_code)
        print("Tokens:", tokens)
        # Further processing like parsing and code generation goes here

# Usage in main.py would change to:
# compiler = Compile(source_code)
# compiler.compile()

