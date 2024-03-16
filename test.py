import re

code = '''
#This-is-comment
#Another comment
#This thing will not be read
sup
'''

match = re.findall(r"\#[\S]+", code, flags=re.MULTILINE)
print(match)
for m in match:
    code = code.replace(m, "")
# [code.replace(x, "") for x in match]
print(code)