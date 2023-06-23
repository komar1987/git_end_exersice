from example import add
from example import subtract
from example import multiply
from example import divide

def test_add():
        assert add(20,30) == 50

def test_subtract():
        assert abs(subtract(32.56,10)-22.56) < 0.001

def test_divide():
        assert divide (100 , 2) == 50
        
def test_sum():
        assert sum(20,56) == 1406 

