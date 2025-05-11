class MatrixDecl:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Transpose:
    def __init__(self, value):
        self.value = value


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Var:
    def __init__(self, name):
        self.name = name

class MatrixLiteral:
    def __init__(self, rows):
        self.rows = rows

class Program:
    def __init__(self, statements):
        self.statements = statements


