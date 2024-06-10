from sqlalchemy.future import select  # Import select from SQLAlchemy

from database import new_session, TaskOrm
from schemas import STaskAdd


class TaskRepository:
    @staticmethod
    async def add_task(task: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @staticmethod
    async def get_tasks() -> list[STaskAdd]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskAdd.model_validate(task) for task in task_models]
            return task_schemas

