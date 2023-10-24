#from calc.methods import stringops as so
from calc.methods import mathops as ma


def main():
#expression = "2.45+45-34.2*(43.43+5)/34.32"
    expression="(45+5)/(28-3)+10*(2+8)"
    try:
        result = ma.evaluate_expression(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

    



   

if __name__ == "__main__":
    main()
