import sys
from Compiler import *
from Parser import *

if len(sys.argv) < 2:
    print("Error: Please provide a filename as a command-line argument.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        contents = file.read()
    parser = Parser()
    compiler = Compiler()
    AST = parser.parse(contents)
    code = compiler.handle_block(AST, 0)
    filename = filename.split(".")[0]
    print(filename)
    with open(filename + ".py", 'w') as file:  # Open in text mode ('w')
        file.write(code)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
