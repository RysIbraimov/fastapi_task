from typing import Annotated
from fastapi import Depends, APIRouter

from schemas import STaskAdd, STaskId
from repository import TaskRepository

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STaskAdd]:
    tasks = await TaskRepository.get_tasks()
    return tasks
