import ast
from flask import Flask, request, jsonify, render_template
from typing import Union, List
import operator

app = Flask(__name__)

# Node data structure for the AST
class Node:
    def __init__(self, type: str, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        node_dict = {
            "type": self.type,
            "value": self.value,
        }
        if self.left:
            node_dict["left"] = self.left.to_dict()
        if self.right:
            node_dict["right"] = self.right.to_dict()
        return node_dict

    @classmethod
    def from_dict(cls, data):
        if data is None:
            return None
        left = cls.from_dict(data.get("left"))
        right = cls.from_dict(data.get("right"))
        return cls(type=data["type"], value=data.get("value"), left=left, right=right)

# Function to create a rule from a rule string
def create_rule(rule_string):
    tokens = rule_string.replace("(", " ( ").replace(")", " ) ").split()
    return parse_expression(tokens)

# Parse tokens into an AST
def parse_expression(tokens):
    def parse_term():
        token = tokens.pop(0)
        if token == '(':
            node = parse_expression(tokens)
            tokens.pop(0)  # Remove closing parenthesis
            return node
        else:
            return parse_condition(token, tokens)

    def parse_condition(token, tokens):
        condition = [token]
        while tokens and tokens[0] not in ("AND", "OR", ")"):
            condition.append(tokens.pop(0))
        return Node(type="operand", value=' '.join(condition))

    node = parse_term()
    while tokens and tokens[0] in ("AND", "OR"):
        operator = tokens.pop(0)
        right = parse_term()
        node = Node(type="operator", value=operator, left=node, right=right)
    return node

# Evaluate a rule against the given data
def evaluate_rule(ast, data):
    if ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    elif ast.type == "operand":
        return eval_condition(ast.value, data)
    return False

# Helper function to evaluate a condition
def eval_condition(condition, data):
    operators = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
    }
    for op_symbol, op_func in operators.items():
        if op_symbol in condition:
            attribute, value = condition.split(op_symbol)
            attribute = attribute.strip()
            value = value.strip().strip("'")
            if value.isdigit():
                value = int(value)
            return op_func(data.get(attribute), value)
    raise ValueError(f"Invalid condition: {condition}")

# API to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API to create a rule
@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json.get('rule')
    try:
        ast = create_rule(rule_string)
        ast_json = ast.to_dict()
        return jsonify({'ast': ast_json}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# API to view individual ASTs
@app.route('/view_rule', methods=['POST'])
def api_view_rule():
    rule_string = request.json.get('rule')
    try:
        ast = create_rule(rule_string)
        ast_json = ast.to_dict()
        print(ast_json)  # Debug: Print the AST to the terminal
        return jsonify({'ast': ast_json}), 200
    except ValueError as e:
        print(f"Error: {str(e)}")  # Debug: Print any error to the terminal
        return jsonify({'error': str(e)}), 400

# Combine rules into a single AST
def combine_rules(rules):
    if not rules:
        raise ValueError("No rules to combine")
    combined_ast = None
    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node(type="operator", value="AND", left=combined_ast, right=ast)
    return combined_ast

# API to combine rules
@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json.get('rules', [])
    try:
        combined_ast = combine_rules(rules)
        ast_json = combined_ast.to_dict()
        return jsonify({'combined_ast': ast_json}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# API to evaluate a rule against data
@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    ast = request.json.get('ast')
    data = request.json.get('data')
    try:
        ast_node = Node.from_dict(ast)
        result = evaluate_rule(ast_node, data)
        return jsonify({'result': result}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
