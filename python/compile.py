class Compile:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.ast = None

    def run_lexer(self):
        print("Tokenizing the source code...")
        from lexer import Lexer  # Adjust the import as needed
        self.tokens = Lexer(self.source_code)
        print("Tokens:", self.tokens)

    def run_parser(self):
        print("Parsing the tokens...")
        from parser import Parser  # Adjust the import as needed
        parser = Parser(self.tokens)
        self.ast = parser.parse()
        print("AST:", self.ast)

    def run_semantic_analysis(self):
        print("Performing semantic analysis...")
        from semantic_analyzer import SemanticAnalyzer  # Adjust the import as needed
        analyzer = SemanticAnalyzer(self.ast)
        analyzer.analyze()  # This will raise an exception if a semantic error is found

    def run_code_generation(self):
        print("Generating C code...")
        from code_generator import CodeGenerator
        code_generator = CodeGenerator(self.ast)
        self.generated_code = code_generator.generate()
        print("Generated C code:\n", self.generated_code)

    def compile(self):
        try:
            self.run_lexer()
            self.run_parser()
            self.run_semantic_analysis()  # Include semantic analysis after parsing
            self.run_code_generation()
        except SyntaxError as e:
            print(f"Compilation error: {e}")

