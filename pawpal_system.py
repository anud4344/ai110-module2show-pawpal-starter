"""Class skeletons for PawPal+, based on diagrams/uml.mmd.

No scheduling logic is implemented yet. This is just the structure.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str = ""
    completed: bool = False

    def mark_complete(self):
        pass

    def update_priority(self, new_priority: str):
        pass

    def get_summary(self) -> str:
        return ""


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def get_tasks(self) -> list:
        return []


@dataclass
class Owner:
    name: str
    available_time: int = 0
    preferences: dict = field(default_factory=dict)

    def update_preferences(self, preferences: dict):
        pass

    def set_available_time(self, minutes: int):
        pass


class Scheduler:
    def __init__(self, tasks: list = None, available_time: int = 0):
        self.tasks = tasks if tasks is not None else []
        self.available_time = available_time
        self.schedule = []

    def sort_tasks(self):
        pass

    def build_schedule(self) -> list:
        return []

    def explain_plan(self) -> str:
        return ""
