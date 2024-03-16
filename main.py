from Parser import *
import json
parser = Parser()
code = '''
if (a == 1) {
    "Hello";
}

let a  = 5;'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 