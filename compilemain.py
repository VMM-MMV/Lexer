from paap import *
from Compiler import *

with open("mylang.jora", 'r') as file:
        contents = file.read()
parser = Parser()
compiler = Compiler()
AST = parser.parse(contents)
compiler.getCode(AST)