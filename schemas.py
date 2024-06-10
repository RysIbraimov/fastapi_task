from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str]


class Task(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool
    task_id: int