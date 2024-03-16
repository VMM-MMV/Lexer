import re

code = '''42 43
'''

comments = re.findall(r'\A\d+', code, flags=re.MULTILINE)
print(comments)