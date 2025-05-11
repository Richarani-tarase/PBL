from lark.tree import Tree
from compiler.ast import MatrixDecl, Assignment,Program

def check_semantics(program):
    if not isinstance(program, Program):
        raise Exception("Semantic Error: Expected a Program node at the root.")
    for stmt in program.statements:
        if not isinstance(stmt, (MatrixDecl, Assignment)):
            raise Exception(f"Semantic Error: Unknown statement type {type(stmt)}")
