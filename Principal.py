#!/usr/bin/env python

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == "__main__":
    file = open("program.c", "r")
    print("Codigo fonte: \n{}".format(file.read()))

    buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []

    print("Analise lexica:")
    for i in buffer.load_buffer():
        t, lex, lin = Analyzer.tokenize(i)
        token += t
        lexeme += lex
        row += lin

    print("\nTokens reconhecidos: {}".format(list(set(token))))