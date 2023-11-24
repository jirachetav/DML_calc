from calc.methods.evaluation.mathops import evaluate_expression
from calc.methods.addition.add import add
from calc.methods.divitions.div import divide
from calc.methods.multiplication.multiply import multiply
from calc.methods.substraction.sub import subtract
from fastapi import FastAPI
import logging 


app=FastAPI()


logging.basicConfig(filename='test_format.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.get("/")
async def root():
    return{"mesdsage":"initial entry"}

@app.get("/addition/{one}/{two}")
async def addition(one: int, two: int):
    add_result=add(one,two)
    logging.info(f" Add: {one} + {two} = {add_result}")
    return{"results": add_result}

@app.get("/substraction/{one}/{two}")
async def substraction(one: int, two: int):
    result=subtract(one,two)
    logging.info(f" Substraction: {one} + {two} = {result}")
    return{"results": result}

@app.get("/multiplication/{one}/{two}")
async def multiplication(one: int, two: int):
    result=multiply(one,two)
    logging.info(f" multiply: {one} + {two} = {result}")
    return{"results": result}

@app.get("/divition/{one}/{two}")
async def divition(one: int, two: int):
    result=divide(one,two)
    logging.info(f" Divide: {one} + {two} = {result}")
    return{"results": result}


@app.get("/operation/{expression}")
async def operation(expression):
    try:
        results=evaluate_expression(expression)
        logging.info(f" operation: {expression} = {results}")
        return{"results": results}
    except Exception as e:
        logging.error(f" error in {expression}")
        return {"result":"error in entry"}

#def main():
#expression = "2.45+45-34.2*(43.43+5)/34.32"
#    expression="(45+5)/(28-3)+10*(2+8)"
#    try:
#        result = evaluate_expression(expression)
#        print("Result:", result)
#    except Exception as e:
#        print("Error:", e)
    
    



   

if __name__ == "__main__":
    main()
