from .repositories import ITaskRepository
from .models import TaskCreate
from fastapi import HTTPException

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Check if task with same title already exists
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task is not None:
            raise HTTPException(
                status_code=400,
                detail=f"Task with title '{task_in.title}' already exists"
            )
        # Business logic could go here
        return self.repo.create(task_in)

    def mark_complete(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if task is None:
            return None
        # Update the task with completed=True
        task.completed = True
        return self.repo.update(task_id, task)