
import os,sys
sys.path.append(os.getcwd())
from stacks import stack
from stacks import Element  
import pytest

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = stack(1)

# Test stack functionality
stack.push(2)
stack.push(3)

@pytest.mark.parametrize("result",[(3),(2),(1)])
def test_pop1(result):    
    assert stack.pop().value == result

@pytest.mark.parametrize("result",[(None)])
def test_pop2(result):    
    assert stack.pop() == result

@pytest.mark.parametrize("result",[(4)])
def test_pop3(result):
    stack.push(4)    
    assert stack.pop().value == result

