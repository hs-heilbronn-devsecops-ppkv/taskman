from fastapi.testclient import TestClient
from taskman.main import app



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_5():
    assert factorial(5) == 120

