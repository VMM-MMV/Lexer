from ELSDParser import *
import json
parser = Parser()
code = '''
pregnancies = 5;
diagnosis = 'Bad';'''

result = parser.parse(code)

print(json.dumps(result, indent=2)) 