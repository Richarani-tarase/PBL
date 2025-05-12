class MatrixDecl:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"MatrixDecl(name={self.name}, value={repr(self.value)})"

    def __eq__(self, other):
        return isinstance(other, MatrixDecl) and self.name == other.name and self.value == other.value


class Transpose:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Transpose(value={repr(self.value)})"

    def __eq__(self, other):
        return isinstance(other, Transpose) and self.value == other.value

class Inverse:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Inverse(value={repr(self.value)})"

    def __eq__(self, other):
        return isinstance(other, Inverse) and self.value == other.value


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment(name={self.name}, value={repr(self.value)})"

    def __eq__(self, other):
        return isinstance(other, Assignment) and self.name == other.name and self.value == other.value


class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp(op={self.op}, left={repr(self.left)}, right={repr(self.right)})"

    def __eq__(self, other):
        return isinstance(other, BinaryOp) and self.op == other.op and self.left == other.left and self.right == other.right


class Var:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var(name={self.name})"

    def __eq__(self, other):
        return isinstance(other, Var) and self.name == other.name


class MatrixLiteral:
    def __init__(self, rows):
        self.rows = rows

    def __repr__(self):
        return f"MatrixLiteral(rows={repr(self.rows)})"

    def __eq__(self, other):
        return isinstance(other, MatrixLiteral) and self.rows == other.rows


class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program(statements={repr(self.statements)})"

    def __eq__(self, other):
        return isinstance(other, Program) and self.statements == other.statements
