# -*- coding: utf-8 -*-


from lexer import Lexer
from indent import Indent


class Parser(Indent):
    
    def __init__(self, verbose=False):
        super().__init__(verbose)
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
    
    def parse(self, filename):
        with open(filename, 'r') as ff:
            self.tokens = self.lexer.lex(ff.readlines())
#            print(self.tokens)
            print("TOKENS : \n", list(map(str, self.tokens)))
            self.tokens = self.remove_comments()
            self.parseProgram()
    
    def acceptIt(self):
        print("AVA : ", self.tokens)
        temp = self.tokens.pop(0)
        print("APRE : ", self.tokens)        
        return temp
    
    def showNext(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
#            sys.exit(1)
    
#    def showNext(self):
#        try:
#            return self.tokens[0]
#        except Exception:
#            raise
    
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
    
    def expect(self, kind):
        temp = self.showNext()
        actual = temp.kind
        if(actual != kind):
            print("Error at {}. Expecting {}, got {}".format(temp.position, kind, actual))
        else:
            return self.acceptIt()
    
    def parseProgram(self):
        self.indent("parseProgram")
        self.expect("INT")
        self.expect("IDENTIFIER")
        self.expect("LPAREN")
        self.expect("RPAREN")
        self.expect("LBRACE")
        self.parseDeclarations()
        self.parseStatements()
        self.expect("RBRACE")
        self.dedent()
        
    def parseDeclarations(self):
        self.indent("parseDeclarations")
        starters = ["INT", "FLOAT", "CHAR"] #TODO : refactor list
        while(self.showNext().kind in starters):
            self.parseDeclaration()
        self.dedent()
    
    def parseDeclaration(self):
        self.indent("parseDeclaration")
        self.parseType()
        self.expect("IDENTIFIER")
        if(self.showNext().equal("LBRACKET")):
            self.acceptIt()
            self.expect("INTEGER_LIT")
            self.expect("RBRACKET")
        while(self.showNext().equal("COMMA")):
            self.acceptIt()
            self.expect("IDENTIFIER")
            if(self.showNext().equal("LBRACKET")):
                self.acceptIt()
                self.expect("INTEGER_LIT")
                self.expect("RBRACKET")
        self.expect("SEMICOLON")
        self.dedent()
    
    def parseType(self):
        temp = ["SEMICOLON", "LBRACE", "IDENTIFIER", "WHILE", "IF"]
        if(self.showNext().kind in temp):
            return self.acceptIt()
        else:
            print("Expecting : {}".format(temp))
    
    def parseStatements(self):
        self.indent("parseStatementS")
        while(self.showNext().kind in ["SEMICOLON", "LBRACE", "IDENTIFIER", "WHILE", "IF"]): #TODO : refactor list ?
            self.parseStatement()
        self.dedent()
        
    def parseStatement(self):
        self.indent("parseStatement")
        actual = self.showNext()
        if(actual.equal("SEMICOLON")):
            self.acceptIt()
        elif(actual.equal("LBRACE")):
            self.parseBlock()
        elif(actual.equal("IDENTIFIER")):
            self.parseAssignement()
        elif(actual.equal("WHILE")):
            self.parseWhile()
        elif(actual.equal("IF")):
            self.parseIf()
        else:
            print("Error parseStatement")
        self.dedent()
        
    def parseAssignement(self):
        self.indent("parseAssignement")
        self.expect("IDENTIFIER")
        if(self.showNext().equal("LBRACKET")):
            self.acceptIt()
            self.parseExpression()
            self.expect("RBRACKET")
        self.expect("ASSIGN")
        self.parseExpression()
        self.expect("SEMICOLON")
        self.dedent()
        
    def parseBlock(self):
        self.indent("parseBlock")
        self.expect("LBRACE")
        self.parseStatements()
        self.expect("RBRACE")
        self.dedent()
    
    def parseIf(self):
        self.indent("parseIf")
        self.expect("IF")
        self.expect("LPAREN")
        self.parseExpression()
        self.expect("RPAREN")
        self.parseStatement()
        if(self.showNext().equal("ELSE")):
            self.acceptIt()
            self.parseStatement()
        
        self.dedent()
    
    def parseWhile(self):
        self.indent("parseWhile")
        self.expect("WHILE")
        self.expect("LPAREN")
        self.parseExpression()
        self.expect("RPAREN")
        self.parseStatement()
        self.dedent()
    
    def parseExpression(self):
        self.indent("parseExpression")
        self.parseConjunction()
        while(self.showNext().equal("DBAR")):
            self.acceptIt()
            self.parseConjunction()
        self.dedent()
    
    def parseConjunction(self):
        self.indent("parseConjunction")
        self.parseEquality()
        while(self.showNext().equal("DAMPERSAND")):
            self.acceptIt()
            self.parseEquality()
        self.dedent()
    
    def parseEquality(self):
        self.indent("parseEquality")
        self.parseRelation()
        while(self.showNext().equal("EQ") or self.showNext().equal("NEQ")):
            self.acceptIt()
            self.parseRelation()
        self.dedent()
    
    def parseRelation(self):
        self.indent("parseRelation")
        self.parseAddition()
        temp = ["LT", "LTE", "GT", "GTE"]
        while(self.showNext().kind in temp):
            self.acceptIt()
            self.parseAddition()
        self.dedent()
    
    def parseAddition(self):
        self.indent("parseAddition")
        self.parseTerm()
        while(self.showNext() in ["ADD", "SUB"]):
            self.acceptIt()
            self.parseTerm()
        self.dedent()
    
    def parseTerm(self):
        self.indent("parseTerm")
        self.parseFactor()
        while(self.showNext().kind in ["MUL", "DIV"]):
            self.acceptIt()
            self.parseFactor()
        self.dedent()
    
    
    def parseFactor(self):
        self.indent("parseFactor")
        if(self.showNext().kind in ["SUB", "NOT"]): # TODO : what is "NOT" ?
            self.acceptIt()
        self.parsePrimary()
        self.dedent()
    
    
    def parsePrimary(self):
        self.indent("parsePrimary")
        nextKind = self.showNext().kind
        if(nextKind == "IDENTIFIER"):
            self.acceptIt()
            if(self.showNext().equal("LBRACKET")):
                self.acceptIt()
                self.parseExpression()
                self.expect("RBRACKET")
        elif(nextKind in ["INTEGER_LIT", "CHAR_LIT", "FLOAT_LIT", "STRING_LIT"]):
            self.acceptIt()
        elif(nextKind == "LPAREN"):
            self.acceptIt()
            self.parseExpression()
            self.expect("RPAREN")
        else:
            print("Expecting {} : got {}".format("truc", nextKind))
        self.dedent()
        
            
        
        
        
























