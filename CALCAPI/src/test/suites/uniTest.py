import sys

sys.path.append("src/calc")
sys.path.append("../")

import pytest

from src.calc.methods.addition.add import add
from src.calc.methods.substraction.sub import subtract
from src.calc.methods.multiplication.multiply import multiply
from src.calc.methods.divitions.div import divide





def datos_add():
        return [(2,2,4), (3,3,6), (7,7,14)]

@pytest.mark.parametrize('a, b, res', datos_add())
def test_add(a,b,res):
        assert  add(a,b) == res




def datos_sub():
        return [(6,2,4), (9,3,6), (14,7,7)]

@pytest.mark.parametrize('a, b, res', datos_sub())
def test_substract(a,b,res):
        assert  subtract(a,b) == res


def datos_mul():
        return [(6,2,12), (9,3,27), (14,2,28)]

@pytest.mark.parametrize('a, b, res', datos_mul())
def test_multiply(a,b,res):
        assert  multiply(a,b) == res


def datos_div():
        return [(12,2,6), (9,3,3), (14,2,7)]

@pytest.mark.parametrize('a, b, res', datos_div())
def test_divide(a,b,res):
        assert  divide(a,b) == res        
