import pytest
import sys

sys.path.append("src/calc")
sys.path.append("../")



from src.calc.methods.evaluation.mathops import evaluate_expression 



 



def datos_int():
        return [("(45+5)/(28-3)+10*(2+8)",102.0), ("(45+5)/(28-3)+10*(2+8)",102.0), ("(45+5)/(28-3)+10*(2+8)",102.0)]

@pytest.mark.parametrize('a, b, res', datos_int())
def test_integration(a,res):
        assert  evaluate_expression(a) == res
        