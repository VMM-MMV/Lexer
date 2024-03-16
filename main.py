from Parser import *
import json
parser = Parser()
code = '''
42 + 32 - 32;'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 