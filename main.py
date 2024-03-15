from Parser import *
import json
parser = Parser()
code = '''
""" 
This is comment
Another comment
'HI' 
"""

40;


40;
"idk";
42;




'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 


'''
""" 
This is comment
Another comment
'HI' 
"""

40;


40;
"idk";
42;




'''