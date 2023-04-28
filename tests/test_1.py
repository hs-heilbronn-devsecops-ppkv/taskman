from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task, delete_tasks
from fastapi.testclient import TestClient
from taskman.main import app



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_2():
    assert factorial(2) == 4

