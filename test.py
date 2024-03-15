import re

code = ''''== 5;\n'
'''

comments = re.findall(r'\A=(?!=)', code, flags=re.MULTILINE)
print(comments)