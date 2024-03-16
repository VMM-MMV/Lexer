from ELSDTokenizer import *

class Parser:
    def parse(self, string):
        self._string = string
        self._tokenizer = Tokenizer(string)

        self._lookahead = self._tokenizer.getNextToken()

        return self.Program()
    
    def Program(self):
        return {
            "type": "Program",
            "body": self.StatementList()
        }
    
    # StatementList : Statement | StatementList Statement ;
    def StatementList(self):
        statementList = []
        
        while self._lookahead != None:
            statementList.append(self.Statement())
        
        return statementList

    # Statement : ExpressionStatement ;
    def Statement(self):
        if self._lookahead["type"] == "DECLARATOR":
            return self.VariableDeclaration()

        return self.ExpressionStatement()
    
    # ExpressionStatement : Expression ';' ;
    def ExpressionStatement(self):
        expression = self.Expression()
        self._eat(";")
        return {
            "type": "ExpressionStatement",
            "expression": expression
        }
    
    def VariableDeclaration(self):
        declaration = self.VariableDeclarator()
        self._eat(";")
        return {
            "type": "VariableDeclaration",
            "declarations": declaration
        }
    
    def VariableDeclarator(self):
        declarator_token = self._eat("DECLARATOR")
        self._eat("DECLARATOR_OPERATOR")
        literal = self.Literal()
        return {
            "type": "VariableDeclarator",
            "id": declarator_token["value"],
            "init": literal
        }
    
    # Expression : Literal ;
    def Expression(self):
        return self.Literal()
    
    # Literal : NumericLiteral | StringLiteral ;
    def Literal(self):
        match self._lookahead["type"]:
            case "STRING": return self.StringLiteral()
            case "NUMBER": return self.NumericLiteral()

    def NumericLiteral(self):
        token = self._eat("NUMBER")
        return {
            "type": "NumericLiteral",
            "value": int(token["value"])
        }
    
    def StringLiteral(self):
        token = self._eat("STRING")
        return {
            "type": "StringLiteral",
            "value": token["value"]
        }
    
    def _eat(self, tokenType):
        token = self._lookahead

        if token == None:
            raise SyntaxError(f"Unexpected end of input, expected {tokenType}.") 
    
        if token["type"] != tokenType:
            print(self._string[self._tokenizer._coursor], self._tokenizer._coursor, self._lookahead)
            val = token["value"]
            raise SyntaxError(f"Unexpected token {val}, expected {tokenType}.")
        
        self._lookahead = self._tokenizer.getNextToken()

        return token