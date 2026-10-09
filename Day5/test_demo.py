def test_f1():
    port = 3000
    assert port == 3000
    
def test_f2():
    host = 3000
    assert port > 3000
    
def test_f3():
    app = "grafana"
    assert app == "grafana"
    
def test_f4():
    n = 100
    assert n < 100
    
    
def test_sample():
    status_code = 200
    assert status_code == 200
    
def test_sample_url():
    url = "api.com"        
    assert url == "api.com"
    
    
# in terminal type -> python -m pytest test_demo.py

    
