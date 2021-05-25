import re
import sys

class LexicalAnalyzer:
    lin_num = 1
    lin_start = 0

    token = []
    lexeme = []
    row = []
    column = []


    def parse(self, m, token_type, token_lexeme):
        print("{0} e {1}".format(m.start(), self.lin_start))
        col = m.start() - self.lin_start
        self.column.append(col)
        self.token.append(token_type)
        self.lexeme.append(token_lexeme)
        self.row.append(self.lin_num)
        print('Token = {0}, Simbolo= \'{1}\', Linha = {2}, Coluna = {3}'.format(token_type, token_lexeme, self.lin_num, col))

    def tokenize(self, code):

        rules = [
            ('MAIN', r'main'),          # main
            ('SPACE', r'[ *]'),         # space 
            ('INT', r'int'),            # int
            ('FLOAT', r'float'),        # float
            ('DOUBLE', r'double'),      # double
            ('CHAR', r'char'),          # char
            ('IF', r'if'),              # if
            ('ELSE', r'else'),          # else
            ('WHILE', r'while'),        # while
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # >=
            ('AND', r'&&'),             # &&
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('OR', r'\|\|'),            # ||
            ('DIV', r'\/'),             # /
            ('ID', r'[a-zA-Z]\w*'),     # IDENTIFIERS
            ('FLOAT_CONST', 
            r'\d(\d)*\.\d(\d)*'),       # FLOAT
            ('INTEGER_CONST', 
            r'\d(\d)*'),                # INT
            ('NEWLINE', r'\n'),         # NEW LINE
            ('MISMATCH', r'[. |]'),     # DOT and PIPE 
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                self.lin_start = m.end()
                self.lin_num += 1
            elif token_type == 'COMMENT':
                continue
            elif token_type == 'MISMATCH':
                sys.exit('ERROR: %r unexpected on line %d' % (token_lexeme, self.lin_num))
            else:
                self.parse(m, token_type, token_lexeme)

        return self.token, self.lexeme, self.row, self.column