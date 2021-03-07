import pytest

def add(a,b):
    return a-b

class Test_Cal():
    def setup(self):
        print("开始计算")
    @pytest.mark.parametrize("a,b",[(8,9),(6,3),(3,7)])
    def test_add(self,a,b):
        assert add(a,b)==a-b


