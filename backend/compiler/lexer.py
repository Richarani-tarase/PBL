from lark import Lark

grammar = r"""
start: statement*

statement: matrix_decl | assignment

matrix_decl: "matrix" CNAME "=" matrix_literal
assignment: CNAME "=" expr

?expr: expr "+" term   -> add
     | expr "-" term   -> sub
     | term

?term: term "*" factor -> mul
     | term "/" factor -> div
     | factor

?factor:factor "." "T"->transpose
       | CNAME         -> var
       | NUMBER        -> number
       | matrix_literal
       | "(" expr ")"

matrix_literal: "[" row ( ";" row )* "]"
row: NUMBER ("," NUMBER)*

%import common.CNAME
%import common.NUMBER
%import common.WS
%ignore WS
"""

parser = Lark(grammar, parser='lalr')
