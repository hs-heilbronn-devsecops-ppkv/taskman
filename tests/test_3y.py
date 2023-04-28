from fastapi.testclient import TestClient
from taskman.main import app
import time
import datetime




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_4():
    print("Running fact of 4",datetime.datetime.now())
    assert factorial(4) == 24

