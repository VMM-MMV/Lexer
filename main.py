from Parser import *
import json
parser = Parser()
code = '''
if (a == 1) {
    "Hello";
} else if (a == 2) {
    "Bye";
} else if (a == 3) {
    "Bye2";
} else {
    "IDK";
}
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 