# fixtures 

import pytest

@pytest.fixture
def input_data():
    var = 40
    return var

def test_divisible_by_3(input_data):
    assert input_data % 3 == 0
    
def test_divisible_by_5(input_data):
    assert input_data % 5 == 0
    
    
    
# to run in Terminal :     
# python -m pytest test_demo4.py -v
