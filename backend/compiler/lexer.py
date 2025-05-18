import re
from collections import namedtuple

# Define the token structure
Token = namedtuple('Token', ['type', 'value', 'position'])

# Define all token types and patterns
TOKEN_SPEC = [
    ('MATRIX',    r'\bmatrix\b'),
    ('INV',       r'\binv\b'),       # <-- Add this
    ('TRANSPOSE', r'\bT\b'),         # <-- Add this too
    ('DET',       r'\bdet\b'), 
    ('IDENT',     r'[A-Za-z_][A-Za-z0-9_]*'),  # Must come after INV and TRANSPOSE
    ('EQUAL',     r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('TIMES',     r'\*'),
    ('DOT',       r'\.'),
    ('LBRACKET',  r'\['),
    ('RBRACKET',  r'\]'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('COMMA',     r','),
    ('SEMICOLON', r';'),
    ('NUMBER',    r'\d+(\.\d*)?'),
    ('SKIP',      r'[ \t\n]+'),
    ('MISMATCH',  r'.'),
]


# Build master regex
master_regex = re.compile(
    '|'.join(f'(?P<{tok}>{pattern})' for tok, pattern in TOKEN_SPEC)
)

def tokenize(code):
    tokens = []
    line = 1
    column = 1
    pos = 0

    for match in master_regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        start = match.start()
        end = match.end()

        if kind == 'SKIP':
            pass  # ignore whitespace
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character {value!r} at position {start}')
        else:
            token = Token(kind, value, (line, column))
            tokens.append(token)

        # update position
        newlines = value.count('\n')
        if newlines:
            line += newlines
            column = len(value) - value.rfind('\n')
        else:
            column += len(value)

        pos = end

    return tokens