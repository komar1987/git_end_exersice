from example import add

from example import subtract


def test_add():
        assert add(20,30) == 50

def test_subtract():
        assert abs(subtract(32.56,10)-22.56) < 0.001
