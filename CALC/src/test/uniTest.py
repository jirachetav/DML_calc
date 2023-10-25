import pytest
from methods import mathops as ma




def datos_operaciones():
        return [(2,2,4), (3,3,6), (7,7,14)]




@pytest.mark.parametrize('a, b, res', datos_operaciones())
def test_operacion_basica(a,b,res):
        assert  ma.add(a,b) == res







