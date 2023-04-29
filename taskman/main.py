# -*- coding: utf-8 -*-
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel
import json
import redis

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


class TaskRequest(BaseModel):
    name: str
    description: str


class Task(TaskRequest):
    item_id: int


tasks: Dict[str, Task] = {}


@app.get('/tasks')
def get_tasks() -> List[Task]:
    #r = get_redis()
    keys = r.keys()
    print(keys)
    tasks = []
    for key in keys:
        value=json.dump(r.get('tasks:{key}'))
        tasks.append({
            item_id:item_id,
            name: value['name'],
            description: value['description'],
        })
    
    return tasks


@app.get('/tasks/{item_id}')
def get_task(item_id: str) -> Task:
    value=json.dumps(r.get('tasks:{item_id}'))
    return Task(
        item_id=item_id,
        name= value['name'],
        description = value['description'],
    )


@app.put('/tasks/{item_id}')
def update_task(item_id: str, item: TaskRequest) -> None:
    r.set('tasks:{item_id}',json.dump({
        name:item.name,
        description:item.description,
    }))
    r.set("tasks:1",son.dump({
        name:"name",
        description:"name",
    }))
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )


@app.post('/tasks')
def create_task(item: TaskRequest):
    item_id = str(len(tasks) + 1)
    r.set("task:{item_id}", json.dump({
        name:item.name,
        description:item.description,
    }))
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )


def delete_tasks():
    tasks.clear()