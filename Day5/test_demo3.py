# pytest with markers

import pytest
@pytest.mark.integration
def test_database_connection():
    assert True
    
@pytest.mark.integration
def test_api_databse_flow():
    assert True
    
    
@pytest.mark.slow
def test_large_file_processing():
    assert True
    
def test_fx():
    assert True 
    
# in Terminal -> python -m pytest .\test_demo3.py -m integration
# in Terminal -> python -m pytest .\test_demo3.py -m slow
# in Terminal -> python -m pytest .\test_demo3.py -m "not slow"
