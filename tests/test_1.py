from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task, delete_tasks
from fastapi.testclient import TestClient
from taskman.main import app
import time
import datetime



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_2():
    print("Running fact of 2", datetime.datetime.now() )
    assert factorial(2) == 2

