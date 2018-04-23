import sys
from indent import Indent


class Parser:

    TYPE = ['INT', 'FLOAT', 'CHAR']
    STATEMENT_STARTERS = ['SEMICOLON', 'LBRACE', 'IDENTIFIER', 'IF', 'WHILE']
    ASSIGN = ["ASSIGN"]
    REL_OP = ['LT', 'LTE', 'GT', 'GTE']
    MUL_OP = ['MUL', 'DIV']
    LITERAL = ['INTEGER_LIT', 'FLOAT_LIT', 'CHAR_LIT']
    EQU_OP = ['EQU', 'NEQ']
    ADD_OP = ['ADD', 'SUB']
    UNARY_OP = ['SUB']


    def __init__(self, verbose=False):
        self.indentator = Indent(verbose)
        self.tokens = []
        self.errors = 0

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if actualKind == kind:
            return self.accept_it()
        else:
            print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
            self.errors += 1
            sys.exit(1)

    # same as expect() but no error if not correct kind
    def maybe(self, kind):
        if self.show_next().kind == kind:
            return self.accept_it()

    def accept_it(self):
        token = self.show_next()
        output = str(token.kind) + ' ' + token.value
        self.indentator.say(output)
        return self.tokens.pop(0)

    def remove_comments(self):
        result = []
        in_comment = False
        for token in self.tokens:
            if token.kind == 'COMMENT':
                pass
            elif token.kind == 'LCOMMENT':
                in_comment = True
            elif token.kind == 'RCOMMENT':
                in_comment = False
            else:
                if not in_comment:
                    result.append(token)
        return result

    def parse(self, tokens):
        self.tokens = tokens
        self.tokens = self.remove_comments()
        self.parse_program()


    def parse_program(self):
        self.indentator.indent('Parsing Program')
        self.expect('INT')
        self.expect('IDENTIFIER')
        self.expect('LPAREN')
        self.expect('RPAREN')
        self.expect('LBRACE')

        self.parse_declarations()
        self.parse_statements()

        self.expect('RBRACE')
        self.indentator.dedent()
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')

    def parse_declarations(self):
        self.indentator.indent('Parsing Declarations')
        while(self.show_next().kind in self.TYPE):
            self.parse_declaration()

        while(self.show_next().kind in self.STATEMENT_STARTERS):
            self.parse_statement()

        self.indentator.dedent()

    def parse_declaration(self):
        self.indentator.indent('Parsing Declaration')
        if(self.show_next().kind in self.TYPE):
            self.accept_it()
        self.expect('IDENTIFIER')
        if (self.show_next().kind == 'LBRACKET'):
            self.accept_it()
            self.expect('INTEGER_LIT')
            self.expect('RBRACKET')

        while(self.show_next().kind == 'COMMA'):
            self.accept_it()
            self.expect('IDENTIFIER')
            if (self.show_next().kind == 'LBRACKET'):
                self.accept_it()
                self.expect('INTEGER_LIT')
                self.expect('RBRACKET')

        self.expect('SEMICOLON')

        self.indentator.dedent()

    def parse_statements(self):
        self.indentator.indent('Parsing Statements')
        while(self.show_next().kind in self.STATEMENT_STARTERS):
            print("KIND = ", self.show_next().kind)
            self.parse_statement()
        self.indentator.dedent()

    def parse_statement(self):
        self.indentator.indent('Parsing Statement')
        print(self.tokens[-1].value)
        print(self.tokens[-1].position)

        if(self.show_next().kind == 'IF'):
            self.parse_if

        if(self.show_next().kind == 'WHILE'):
            self.parse_while

        if(self.show_next().kind == 'SEMICOLON'):
#            self.expect('SEMICOLON')
            self.accept_it()
#            self.indentator.dedent()

        if(self.show_next().kind == 'LBRACE'):
            self.parse_block

        if(self.show_next().kind == 'IDENTIFIER'):
            self.parse_assignement

        self.indentator.dedent()

    def parse_block(self):
        self.indentator.indent('Parsing Block')
        self.expect('LBRACE')
#        self.accept_it()
        self.parse_statements()
        self.expect('RBRACE')
        self.indentator.dedent()

    def parse_assignement(self):
        self.indentator.indent('Parsing Assignement')
        self.expect('IDENTIFIER')
#        self.accept_it()
        if (self.show_next().kind == 'LBRACKET'):
            self.accept_it()
            self.parse_expression()
            self.expect('RBRACKET')
        self.expect('ASSIGN')
        self.parse_expression()
        self.expect("SEMICOLON")
        print("!!!!!! here !!!!!!")
        s
        self.indentator.dedent()

    def parse_if(self):
        self.indentator.indent('Parsing If')
        self.expect('IF')
        self.accept_it()
        self.expect('LPAREN')
        self.parse_expression()
        self.expect('RPAREN')
        self.parse_statement()
        if(self.show_next().kind == 'ELSE'):
            self.accept_it()
            self.parse_statement()
        self.indentator.dedent()

    def parse_while(self):
        self.indentator.indent('Parsing While')
        self.expect('WHILE')
#        self.accept_it()
        self.expect('LPAREN')
        self.parse_expression()
        self.expect('RPAREN')
        self.parse_statement()
        self.indentator.dedent()
#        self.indentator.dedent()

    def parse_expression(self):
        self.indentator.indent('Parsing Expression')
        self.parse_conjunction()
        while(self.show_next().kind == 'DBAR'):
            self.accept_it()
            self.parse_conjunction()
        self.indentator.dedent()

    def parse_conjunction(self):
        self.indentator.indent('Parsing Conjunction')
        self.parse_equality()
        while(self.show_next().kind == 'DAMPERSAND'):
            self.accept_it()
            self.parse_equality()
        self.indentator.dedent()

    def parse_equality(self):
        self.indentator.indent('Parsing Equality')
        self.parse_relation()
        if (self.show_next().kind in self.EQU_OP):
            self.accept_it()
            self.parse_relation()
        self.indentator.dedent()

    def parse_relation(self):
        self.indentator.indent('Parsing Relation')
        self.parse_addition()
        if(self.show_next().kind in self.REL_OP):
            self.accept_it()
            self.parse_addition()
        self.indentator.dedent()

    def parse_addition(self):
        self.indentator.indent('Parsing Addition')
        self.parse_terme()
        while(self.show_next().kind in self.ADD_OP):
            self.accept_it()
            self.parse_terme()
        self.indentator.dedent()

    def parse_terme(self):
        self.indentator.indent('Parsing Terme')
        self.parse_factor()
        while(self.show_next().kind in self.MUL_OP):
            self.accept_it()
            self.parse_factor()
        self.indentator.dedent()

    def parse_factor(self):
        self.indentator.indent()
        if (self.show_next().kind in self.UNARY_OP):
            self.accept_it()
            self.parse_primary()
        else:
            self.parse_primary()
        self.indentator.dedent()

    def parse_primary(self):
        self.indentator.indent()
#        self.expect("IDENTIFIER")
#        kind = self.show_next().kind
#        if kind == "IDENTIFIER":
#            self.accept_it()
#            if self.show_next().kind == "LBRACKET":
#                self.accept_it()
#                self.parse_expre




        while(self.show_next().kind == "LBRACKET"):
            self.accept_it()
            if(self.show_next().kind == "LBRACKET"):
                self.accept_it()
                self.parse_expression()
                self.expect("RBRACKET")
        while(self.show_next().kind in self.LITERAL):
            self.accept_it()

        while(self.show_next().kind == "LPAREN"):
            self.accept_it()
            self.parse_expression
            self.expect("RPAREN")

        self.indentator.dedent()










