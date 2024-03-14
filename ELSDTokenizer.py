import re

Tokens = [
    # [r"^\s+", "WHITESPACE"],
    # # [r"^\n+", "NEWLINE"],
    # # [r'^\""".*?"""', "COMMENT"],
    # [r"^\#.*$", "COMMENT"],
    # [r"^;" , ";"],
    # [r"^\d+", "NUMBER"],
    [r"^pregnancies,", "Pregnancies"],
    [r"^diagnosis" , 'Diagnosis'],
    [r"^treatment" , 'Treatment'],
    [r"^pregnancies" , 'Pregnancies'],
    [r"^glucose" , 'Glucose'],
    [r"^bloodPressure" , 'BloodPressure'],
    [r"^skinThickness" , 'SkinThickness'],
    [r"^insulin" , 'Insulin'],
    [r"^bmi" , 'BMI'],
    [r"^diabetesPedigreeFunction", 'DiabetesPedigreeFunction'],
    [r"^age", 'Age'],
    [r"^outcome", 'Outcome'],
    [r"^[a-zA-Z]+", "ID"],
    [r"^[0-9]+", "INT"],
    [r"^[0-9]+(\.[0-9]+)?", "FLOAT"],
    [r'^ \"(~[\"\r\n])*\" ;$"', "TEXT"],
    # [r'^\"(?:[^"\\]|\\.)*"', "STRING"],
    # [r"^\'(?:[^'\\]|\\.)*'", "STRING"],
]

class Tokenizer:
    def __init__(self, string):
        self._string = string
        self._coursor = 0
    
    def hasMoreTokens(self):
        return self._coursor < len(self._string)
    
    def getNextToken(self):
        if not self.hasMoreTokens():
            return None
        
        curr_string = self._string[self._coursor:]

        for regex, literal_type in Tokens:
            match = re.findall(regex, curr_string, flags=re.MULTILINE)
            
            if len(match) == 0:
                continue

            if literal_type in ["WHITESPACE", "COMMENT"]:
                self._coursor += len(match[0])
                return self.getNextToken()
            
            self._coursor += len(match[0])
            return {
                "type": literal_type,
                "value": match[0]
            }
