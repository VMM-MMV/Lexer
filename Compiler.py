class Compiler:
    # def __init__(self):
    #     self.string = AST
    #     print(self.string)

    def handle_literal(self, node):
        match node["type"]:
            case "NumericLiteral": return int(node["value"])
            case "StringLiteral": return f'"{node["value"]}"' 

    def handleIf(self, node):
        def handle_boolean_statement(node):
            boolean_statement = ""
            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                        boolean_statement += " " + str(value["value"])
            return boolean_statement + ":"
        
        if_code = "if"
        node = node["BooleanStatement"]
       
        if_code += " " + handle_boolean_statement(node)
        print(if_code)


    
    def getCode(self, node):
        code = ""
        def walk_ast(node, indent=0):
            if node is None:
                return

            print(" " * indent + node['type'])
            if node["type"] == "IfStatement":
                self.handleIf(node)

            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                    walk_ast(value, indent + 2)  # Child node
                elif key != 'type' and isinstance(value, list):
                    for item in value:
                        walk_ast(item, indent + 2)  # Items within a list
            
        walk_ast(node)

