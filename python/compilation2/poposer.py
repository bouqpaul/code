# -*- coding: utf-8 -*-


from lexer import Lexer
from indent import Indent


class Parser(object, Indent):
    
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
    
    def parse(self, filename):
        with open(filename, 'r') as ff:
            self.lexer.lex(ff.readlines())
            self.parseProgram()
    
    def acceptIt(self):
        pass
    
    def showNext(self):
        try:
            return self.tokens[-1]
        except Exception:
            raise
    
    def expect(self, kind):
        actual = self.showNext().kind
        if(actual != kind):
            print("Expecting {}, got {}".format(kind, actual))
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
        starters = ["INT", "FLOAT", "CHAR"]
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
            
        
        
        
























