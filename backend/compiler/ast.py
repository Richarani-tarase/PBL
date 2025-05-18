class MatrixDecl:
    def _init_(self, name, value):
        self.name = name
        self.value = value

    def _repr_(self):
        return f"MatrixDecl(name={self.name}, value={repr(self.value)})"

    def _eq_(self, other):
        return isinstance(other, MatrixDecl) and self.name == other.name and self.value == other.value

class Determinant:
    def _init_(self, matrix_expr):
        self.matrix_expr = matrix_expr

class Transpose:
    def _init_(self, value):
        self.value = value

    def _repr_(self):
        return f"Transpose(value={repr(self.value)})"

    def _eq_(self, other):
        return isinstance(other, Transpose) and self.value == other.value

class Inverse:
    def _init_(self, value):
        self.value = value

    def _repr_(self):
        return f"Inverse(value={repr(self.value)})"

    def _eq_(self, other):
        return isinstance(other, Inverse) and self.value == other.value


class Assignment:
    def _init_(self, name, value):
        self.name = name
        self.value = value

    def _repr_(self):
        return f"Assignment(name={self.name}, value={repr(self.value)})"

    def _eq_(self, other):
        return isinstance(other, Assignment) and self.name == other.name and self.value == other.value


class BinaryOp:
    def _init_(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def _repr_(self):
        return f"BinaryOp(op={self.op}, left={repr(self.left)}, right={repr(self.right)})"

    def _eq_(self, other):
        return isinstance(other, BinaryOp) and self.op == other.op and self.left == other.left and self.right == other.right


class Var:
    def _init_(self, name):
        self.name = name

    def _repr_(self):
        return f"Var(name={self.name})"

    def _eq_(self, other):
        return isinstance(other, Var) and self.name == other.name


class MatrixLiteral:
    def _init_(self, rows):
        self.rows = rows

    def _repr_(self):
        return f"MatrixLiteral(rows={repr(self.rows)})"

    def _eq_(self, other):
        return isinstance(other, MatrixLiteral) and self.rows == other.rows


class Program:
    def _init_(self, statements):
        self.statements = statements

    def _repr_(self):
        return f"Program(statements={repr(self.statements)})"

    def _eq_(self, other):
        return isinstance(other, Program) and self.statements == other.statements