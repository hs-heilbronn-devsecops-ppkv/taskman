from fakeredis import FakeStrictRedis
from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task
from fastapi.testclient import TestClient
from taskman.main import app
import time


def test_save_and_get_item():
    r = FakeStrictRedis()
    id = create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), r)
    assert get_task(id, r) == Task(name='Test Task', description='Demo', id=id)

#test api for getting tasks
def test_get_tasks():
    client = TestClient(app)
    response = client.get("/tasks")
    print("Running test for get task api")
    assert response.status_code == 200


def test_save_and_get_items():
    r = FakeStrictRedis()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), r)
    create_task(TaskRequest(
        name='Test Task 2',
        description='Demo 2',
    ), r)
    tasks = get_tasks(r)
    assert len(tasks)==2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_3():
    print("Running fact of 3")
    assert factorial(3) == 6

