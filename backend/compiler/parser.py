from lark import Lark, Transformer
from compiler.ast import *
from numbers import Number

grammar = r"""
    start: statement+
    statement: matrix_decl | assignment

    matrix_decl: "matrix" CNAME "=" matrix_literal
    assignment: CNAME "=" expr

    ?expr: expr "+" term   -> add
        | expr "-" term   -> sub
        | term

    ?term: term "*" factor -> mul
        | factor

    ?factor: transposable
        | "(" expr ")"

    ?transposable: atom "." "T" -> transpose
        | atom

    ?atom: CNAME         -> var
        | matrix_literal
        | NUMBER        -> number

    matrix_literal: "[" row (";" row)* "]"
    row: NUMBER ("," NUMBER)*

    %import common.CNAME
    %import common.NUMBER
    %import common.WS
    %ignore WS

"""

parser = Lark(grammar, parser='lalr')

class ASTTransformer(Transformer):
    def start(self, items):
        return Program(items)

    def statement(self, items):
        return items[0]

    def matrix_decl(self, items):
        name, matrix = items
        return MatrixDecl(name, matrix)

    def assignment(self, items):
        name, expr = items
        return Assignment(name, expr)

    def add(self, items):
        return BinaryOp('+', items[0], items[1])

    def sub(self, items):
        return BinaryOp('-', items[0], items[1])
    
    def mul(self, items):
        return BinaryOp('*', items[0], items[1])
    
    def transpose(self, items):
        return Transpose(items[0])


    def var(self, items):
        return Var(str(items[0]))

    def number(self, items):
        return Number(float(items[0]))

    def matrix_literal(self, items):
        return MatrixLiteral(items)

    def row(self, items):
        return [float(x) for x in items]

def parse_code(code):
    tree = parser.parse(code)
    return ASTTransformer().transform(tree)
