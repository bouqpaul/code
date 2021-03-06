import sys
import argparse
from lexer import Lexer


from paparser import Parser
#from poposer import Parser


from totoken import Token


if __name__ == '__main__':

    # adding test file name as command line argument
#    argParser = argparse.ArgumentParser()
#    argParser.add_argument('testFileName')
#    args = argParser.parse_args()
#
#    testFileName = args.testFileName
    testFileName = "test.c"
    try:
        with open(testFileName, 'r') as testFile:
            testFileData = testFile.readlines()

    except FileNotFoundError:
        print('Error: test file {} does not exist'.format(testFileName))
        sys.exit()

    lexer = Lexer()
    tokens = lexer.lex(testFileData)
#
    verbose = True
    parser = Parser(verbose)
#    parser.parse("test.c")
    parser.parse(tokens)
    
    
    
    
#    verbose = True
#    parser = Parser(verbose)
#    parser.parse("test.c")