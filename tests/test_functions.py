from app.functions import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add('b', 'c') == 'bc'

def test_subtract():
    assert subtract(2, 3) == -1