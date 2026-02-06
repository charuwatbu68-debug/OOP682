from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate
from .models_orm import TaskORM
from sqlalchemy.orm import Session


class ITaskRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task_id: int, task: Task) -> Optional[Task]:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Task]:
        pass

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(
            id=self.current_id,
            **task_in.dict()
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task_id: int, task: Task) -> Optional[Task]:
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task_id:
                self.tasks[i] = task
                return task
        return None

    def get_by_title(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None


class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        tasks_orm = self.db.query(TaskORM).all()
        return [Task.from_orm(task_orm) for task_orm in tasks_orm]

    def create(self, task_in: TaskCreate) -> Task:
        task_orm = TaskORM(**task_in.dict())
        self.db.add(task_orm)
        self.db.commit()
        self.db.refresh(task_orm)
        return Task.from_orm(task_orm)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        task_orm = self.db.query(TaskORM).filter(TaskORM.id == task_id).first()
        if task_orm is None:
            return None
        return Task.from_orm(task_orm)

    def update(self, task_id: int, task: Task) -> Optional[Task]:
        task_orm = self.db.query(TaskORM).filter(TaskORM.id == task_id).first()
        if task_orm is None:
            return None
        
        for field, value in task.dict(exclude={'id'}).items():
            setattr(task_orm, field, value)
        
        self.db.commit()
        self.db.refresh(task_orm)
        return Task.from_orm(task_orm)

    def get_by_title(self, title: str) -> Optional[Task]:
        task_orm = self.db.query(TaskORM).filter(TaskORM.title == title).first()
        if task_orm is None:
            return None
        return Task.from_orm(task_orm)