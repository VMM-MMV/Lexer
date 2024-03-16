from Parser import *
import json
parser = Parser()
code = '''
let a = 2 + 32 * 32;
a + b;'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 