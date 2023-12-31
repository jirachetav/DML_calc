from calc.methods.addition.add import add
from calc.methods.substraction.sub import subtract
from calc.methods.multiplication.multiply import multiply
from calc.methods.divitions.div import divide

def evaluate_expression(expression):
    """

    Args:
      expression: es una expresión del tipo (4+3)/(4-5)

    Returns: el valor calculado de la expreción 

    """
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    operator_functions = {'+': add, '-': subtract, '*': multiply, '/': divide}
    values = []
    operators_stack = []
    
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i - 1] in ('(', '+', '-', '*', '/'))):
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            values.append(float(expression[i:j]))
            i = j
        elif expression[i] in operators:
            while (operators_stack and operators_stack[-1] in operators and
                   operators[operators_stack[-1]] >= operators[expression[i]]):
                right = values.pop()
                left = values.pop()
                op = operators_stack.pop()
                result = operator_functions[op](left, right)
                values.append(result)
            operators_stack.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators_stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators_stack[-1] != '(':
                right = values.pop()
                left = values.pop()
                op = operators_stack.pop()
                result = operator_functions[op](left, right)
                values.append(result)
            operators_stack.pop()  # Remove the '('
            i += 1
        else:
            raise ValueError("Invalid character in the expression")
    
    while operators_stack:
        right = values.pop()
        left = values.pop()
        op = operators_stack.pop()
        result = operator_functions[op](left, right)
        values.append(result)
    
    return values[0]