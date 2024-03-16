from Parser import *
import json
parser = Parser()
code = '''
let a = 2 + 32 * 42;
a == b + a;'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 