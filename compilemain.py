from paap import *
from Compiler import *
import json

with open("mylang.jora", 'r') as file:
        contents = file.read()
parser = Parser()
compiler = Compiler()
AST = parser.parse(contents)
compiler.handle_block(AST)
# print(json.dumps(AST, indent=2))