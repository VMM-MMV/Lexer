import re
import autopep8
class Compiler:
    def get_indent(self, indent):
        return " " * indent

    def handle_binary_expression(self, node):
        if not node:
            return
        
        if node.get("expression"):
            node = node["expression"]

        print(node)
        if node["type"] == "BinaryExpression":
            return f"({self.handle_binary_expression(node['left'])} {self.handle_binary_expression(node['operator'])} {self.handle_binary_expression(node['right'])})"
        else:
            return str(node["value"])
    
    def handle_variable_declaration(self, node, indent):
        node = node["declarations"]
        return self.get_indent(indent) + f"{node['id']['value']} = {self.handle_binary_expression(node['init'])}"
        
    def handleIf(self, node, indent):
        if_code = "\n" + self.get_indent(indent) + "if"
        if node.get("BooleanStatement"):
            if_code += " " + self.handle_binary_expression(node["BooleanStatement"]) + ":"

        if node.get("IfBlock"):
            if_code += "\n" + self.get_indent(indent+2) + self.handle_block(node["IfBlock"], indent+2)
        
        if node.get("AlternativeIf"):
            if_code += "\n" + self.get_indent(indent) + "else"
            if_code += "\n" + self.get_indent(indent) + self.handleIf(node["AlternativeIf"], indent)
        
        return if_code
        
    def handle_block(self, node, indent):
        self.code = ""
        def walk_ast(node, indent):
            if node is None:
                return

            try:
                print(node['type'])
            except:
                pass

            if node["type"] == "IfStatement":
                self.code += str(self.handleIf(node, indent))
                return
            
            if node["type"] == "ExpressionStatement":
                self.code += "\n"
                self.code += self.get_indent(indent) + str(self.handle_binary_expression(node))
                return

            if node["type"] == "VariableDeclaration":
                self.code += "\n"
                self.code += self.get_indent(indent) + str(self.handle_variable_declaration(node, indent))
            
            if node["type"] == "PrintStatement":
                self.code += f"print({self.handle_binary_expression(node)})"
                
            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                    walk_ast(value, indent)  # Child node
                elif key != 'type' and isinstance(value, list):
                    for item in value:
                        walk_ast(item, indent)  # Items within a list            
            
        walk_ast(node, indent)
        matches = re.findall(r"else\s+(?:\n\s*)?if\s+\(.*?\):", self.code, flags=re.MULTILINE)
        for matchh in matches:
            print(matchh.find("if"))
            len_of_if = 2
            self.code = self.code.replace(matchh, "elif"+ matchh[matchh.find("if")+len_of_if:])
        matches = re.findall(r"else\s+(?:\n\s*)?if", self.code, flags=re.MULTILINE)
        for matchh in matches:
            print(matchh.find("if"))
            len_of_if = 2
            self.code = self.code.replace(matchh, "else:")
        return self.code

