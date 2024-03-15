import unittest
from Tokenizer import * 
from Parser import *

class TokenizerTests(unittest.TestCase):
    def test_number(self):
        tokenizer = Tokenizer("123;")
        token = tokenizer.getNextToken()
        self.assertEqual(token['type'], 'NUMBER')
        self.assertEqual(token['value'], '123')

    def test_tokenizer(self):
        code = "42;\n10;"
        tokenizer = Tokenizer(code)
        while tokenizer.hasMoreTokens():
            token = tokenizer.getNextToken()
            print(token)

    
class ParserTests(unittest.TestCase):
    def test_numeric_literal(self):
        parser = Parser()
        program = parser.parse("123;")
        self.assertEqual(program, {
        "type": "Program",
        "body": [
            {
            "type": "ExpressionStatement",
            "expression": {
                "type": "NumericLiteral",
                "value": 123
            }
            }
        ]
        })

    def test_variable_declaration(self):
        parser = Parser()
        program = parser.parse("let a = 5;")
        self.assertEqual(program, {
        "type": "Program",
        "body": [
            {
            "type": "VariableDeclaration",
            "declarations": {
                "type": "VariableDeclarator",
                "id": {
                "type": "Identifier",
                "name": "a"
                },
                "init": {
                "type": "NumericLiteral",
                "value": 5
                }
            }
            }
        ]
        })
    
    def test_big_comment(self):
        parser = Parser()
        program = parser.parse('''
        """ 
        This is comment
        Another comment
        This thing will not be read
        """

        40;


        40;
        "idk";
        42;

        ''')
        self.assertEqual(program, {
        "type": "Program",
        "body": [
            {
            "type": "ExpressionStatement",
            "expression": {
                "type": "NumericLiteral",   
                "value": 40
            }
            },
            {
            "type": "ExpressionStatement",
            "expression": {
                "type": "NumericLiteral",
                "value": 40
            }
            },
            {
            "type": "ExpressionStatement",
            "expression": {
                "type": "StringLiteral",
                "value": "\"idk\""
            }
            },
            {
            "type": "ExpressionStatement",
            "expression": {
                "type": "NumericLiteral",
                "value": 42
            }
            }
        ]
        })

        


if __name__ == '__main__':
    unittest.main()
