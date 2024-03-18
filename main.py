from Parser import *
import json
parser = Parser()
code = '''
# let liviu = "Mujik";

if (1) {
    2;
}
 else if (3) {
    4;
# } else if (5) {
#     "Bye2";
} else {
    5;
}
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 