#!/usr/bin/env python

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == "__main__":
    arq = open("program.c", "r")
    print("Codigo fonte: {}".format(arq.read()))

    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []
    column = []

    print("Analise lexica:")
    for i in Buffer.load_buffer():
        t, lex, lin, col = Analyzer.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    print("\nTokens reconhecidos: {}".format(list(set(token))))