from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task, delete_tasks
from fastapi.testclient import TestClient
from taskman.main import app


def test_save_and_get_item():
    delete_tasks()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ))
    assert get_task('1') == Task(name='Test Task', description='Demo', item_id=1)


def test_save_and_get_items():
    delete_tasks()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ))
    create_task(TaskRequest(
        name='Test Task 2',
        description='Demo 2',
    ))
    tasks = get_tasks()
    assert len(tasks)==2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_of_3():
    assert factorial(3) == 6