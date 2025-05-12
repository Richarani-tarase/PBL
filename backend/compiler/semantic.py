from lark.tree import Tree
from compiler.ast import *

def check_expr(expr):
    if isinstance(expr, (Transpose, Inverse)):
        check_expr(expr.value)
    elif isinstance(expr, BinaryOp):
        check_expr(expr.left)
        check_expr(expr.right)
    elif isinstance(expr, (Var, MatrixLiteral, float)):
        return
    else:
        raise Exception(f"Semantic Error: Unsupported expression type {type(expr)}")

def check_semantics(program):
    if not isinstance(program, Program):
        raise Exception("Semantic Error: Expected a Program node at the root.")
    for stmt in program.statements:
        if isinstance(stmt, MatrixDecl):
            continue
        elif isinstance(stmt, Assignment):
            check_expr(stmt.value)
        else:
            raise Exception(f"Semantic Error: Unknown statement type {type(stmt)}")
