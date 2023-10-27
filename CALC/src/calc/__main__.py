from calc.methods.evaluation.mathops import evaluate_expression


def main():
#expression = "2.45+45-34.2*(43.43+5)/34.32"
    expression="(45+5)/(28-3)+10*(2+8)"
    try:
        result = evaluate_expression(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

    



   

if __name__ == "__main__":
    main()
