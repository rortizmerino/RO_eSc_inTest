from example import add

def test_add():
    assert add(1,2) == 3
    return "add works!"

def test_substract():
    assert substract(3,2) == 1
    return "substract works!"
