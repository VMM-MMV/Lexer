from ELSDParser import *
import json
parser = Parser()
code = '''
Preganncies = 5

'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 