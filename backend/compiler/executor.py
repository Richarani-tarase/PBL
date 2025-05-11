import numpy as np
from compiler.ast import *  # Assuming you have the necessary AST classes

def execute(program):
    env = {}

    for stmt in program.statements:
        if isinstance(stmt, MatrixDecl):
            # Ensure that stmt.value.rows is a list of lists (2D matrix)
            env[stmt.name] = np.array(stmt.value.rows)
        elif isinstance(stmt, Assignment):
            env[stmt.name] = evaluate_expression(stmt.value, env)

    return env

def evaluate_expression(expr, env):
    if isinstance(expr, Var):
        return env[expr.name]
    elif isinstance(expr, MatrixLiteral):
        # Matrix literal is a 2D array (list of lists)
        return np.array(expr.rows)
    elif isinstance(expr, Transpose):
        val = evaluate_expression(expr.value, env)
        return np.transpose(val)

    elif isinstance(expr, BinaryOp):
        left = evaluate_expression(expr.left, env)
        right = evaluate_expression(expr.right, env)
        if expr.op == '+':
            return left + right
        elif expr.op == '-':
            return left - right
        elif expr.op == '*':
            return np.matmul(left, right)
        elif expr.op == 'T':  # Handling matrix transpose
            return np.transpose(left)
        else:
            raise Exception(f"Unknown operator {expr.op}")
    else:
        raise Exception(f"Unknown expression type: {type(expr)}")
