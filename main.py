from Parser import *
import json
parser = Parser()
code = '''
# let liviu = "Mujik";

if (1) {
    print(2);
}
 else if (3) {
    print(4);
# } else if (5) {
#     print("Bye2");
} else {
    print(5);
}
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 