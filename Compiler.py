class Compiler:
    # def __init__(self):
    #     self.string = AST
    #     print(self.string)

    def handle_expression(self, node):
        if not node:
            return
        
        if node.get("expression"):
            node = node["expression"]

        if node["type"] == "BinaryExpression":
            return f"({self.handle_expression(node['left'])} {self.handle_expression(node['operator'])} {self.handle_expression(node['right'])})"
        else:
            return str(node["value"])
        
    def handleIf(self, node):
        def handle_boolean_statement(node):
            boolean_statement = ""
            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                        boolean_statement += " " + self.handle_value(value)
            return boolean_statement + ":"

        # def handle_block_statement(node):
            
        
        if_code = ""
        match node["type"]:
            case "IfStatement": 
                if_code += "if"
                node = node["BooleanStatement"]
                if_code += " " + handle_boolean_statement(node)
                node = node["IfBlock"]
                

    
    def handle_block(self, node):
        code = ""
        def walk_ast(node, indent=0):
            if node is None:
                return

            print(" " * indent + node['type'])
            if node["type"] == "IfStatement":
                code += self.handleIf(node)
            
            if node["type"] == "ExpressionStatement":
                print(self.handle_expression(node))
                

            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                    walk_ast(value, indent + 2)  # Child node
                elif key != 'type' and isinstance(value, list):
                    for item in value:
                        walk_ast(item, indent + 2)  # Items within a list            
            
        walk_ast(node)
        return code

