from compiler.ast import *
from compiler.lexer import tokenize

class Parser:
    def _init_(self, code):
        self.tokens = tokenize(code)  # Assuming tokenize is imported from lexer.py
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, kind):
        tok = self.current()
        if tok and tok.type == kind:
            self.pos += 1
            return tok
        return None

    def expect(self, kind):
        tok = self.match(kind)
        if not tok:
            raise SyntaxError(f"Expected {kind} at position {self.pos}")
        return tok

    def parse(self):
        stmts = []
        while self.current():
            stmts.append(self.parse_statement())
        return Program(stmts)

    def parse_statement(self):
        if self.match("MATRIX"):
            name = self.expect("IDENT").value
            self.expect("EQUAL")
            value = self.parse_matrix_literal()
            return MatrixDecl(name, value)
        else:
            name = self.expect("IDENT").value
            self.expect("EQUAL")
            value = self.parse_expr()
            return Assignment(name, value)

    def parse_expr(self):
        # Handle addition and subtraction
        left = self.parse_term()
        while True:
            if self.match("PLUS"):
                right = self.parse_term()
                left = BinaryOp('+', left, right)
            elif self.match("MINUS"):
                right = self.parse_term()
                left = BinaryOp('-', left, right)
            else:
                break
        return left

    def parse_term(self):
        left = self.parse_factor()
        while True:
            if self.match("TIMES"):
                right = self.parse_factor()
                left = BinaryOp('*', left, right)
            else:
                break
        return left

    def parse_factor(self):
        if self.match("LPAREN"):
            expr = self.parse_expr()
            self.expect("RPAREN")
            return expr

        if self.match("LBRACKET"):
            return self.parse_matrix_literal()

        tok = self.current()
        if tok.type == "IDENT":
            var_name = tok.value
            self.pos += 1
            # Check for dot operations like transpose and inverse
            if self.match("DOT"):
                if self.match("TRANSPOSE"):
                    return Transpose(Var(var_name))
                elif self.match("INV"):
                    return Inverse(Var(var_name))
                elif self.match("DET"):
                    return Determinant(Var(var_name))
                else:
                    raise SyntaxError("Unknown property after '.'")

            return Var(var_name)

        elif tok.type == "NUMBER":
            self.pos += 1
            return float(tok.value)

        else:
            raise SyntaxError(f"Unexpected token {tok}")


    def parse_matrix_literal(self):
        self.expect("LBRACKET")
        rows = []
        while True:
            self.expect("LBRACKET")
            row = []
            row.append(float(self.expect("NUMBER").value))
            while self.match("COMMA"):
                row.append(float(self.expect("NUMBER").value))
            self.expect("RBRACKET")
            rows.append(row)
            if self.match("SEMICOLON"):
                continue
            else:
                break
        self.expect("RBRACKET")
        return MatrixLiteral(rows)

def parse_code(code):
    parser = Parser(code)
    return parser.parse()