from paap import *
from Compiler import *
import json

with open("mylang.jora", 'r') as file:
        contents = file.read()
parser = Parser()
compiler = Compiler()
AST = parser.parse(contents)
code = compiler.handle_block(AST, 0)
print(code)
# print(json.dumps(AST, indent=2))