from example import add

from example import subtract
from example import multiply

def test_add():
        assert add(20,30) == 50

def test_subtract():
        assert abs(subtract(32.56,10)-22.56) < 0.001

def multiply():
    assert multiply (100 , 2) == 200