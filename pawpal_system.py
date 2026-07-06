"""Core classes and basic scheduling logic for PawPal+"""

from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str = ""
    completed: bool = False
    scheduled_time: str = ""

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def update_priority(self, new_priority: str):
        """Change this task's priority."""
        self.priority = new_priority

    def get_summary(self) -> str:
        """Return a short readable summary of this task."""
        status = "done" if self.completed else "not done"
        return f"{self.title} ({self.duration_minutes} min, priority: {self.priority}, {status})"


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet's task list if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list:
        """Return this pet's list of tasks."""
        return self.tasks


@dataclass
class Owner:
    name: str
    available_time: int = 0
    preferences: dict = field(default_factory=dict)
    pet: "Pet" = None

    def update_preferences(self, preferences: dict):
        """Update the owner's preferences with new values."""
        self.preferences.update(preferences)

    def set_available_time(self, minutes: int):
        """Set how many minutes the owner has available."""
        self.available_time = minutes


class Scheduler:
    def __init__(self, tasks: list = None, available_time: int = 0, preferences: dict = None):
        self.tasks = tasks if tasks is not None else []
        self.available_time = available_time
        self.preferences = preferences if preferences is not None else {}
        self.schedule = []

    def sort_tasks(self):
        """Sort tasks so higher priority tasks come first."""
        priority_rank = {"high": 0, "medium": 1, "low": 2}
        self.tasks.sort(key=lambda task: priority_rank.get(task.priority, 3))

    def build_schedule(self) -> list:
        """Build a daily schedule by fitting sorted tasks into the available time."""
        self.sort_tasks()
        self.schedule = []
        remaining_time = self.available_time
        elapsed_time = 0

        for task in self.tasks:
            if task.duration_minutes <= remaining_time:
                task.scheduled_time = f"{elapsed_time} min"
                self.schedule.append(task)
                remaining_time -= task.duration_minutes
                elapsed_time += task.duration_minutes

        return self.schedule

    def explain_plan(self) -> str:
        """Return a readable explanation of what was scheduled and what was skipped."""
        if not self.schedule:
            return "No tasks were scheduled."

        lines = ["Daily plan:"]
        for task in self.schedule:
            lines.append(
                f"- {task.scheduled_time}: {task.title} "
                f"({task.duration_minutes} min, priority: {task.priority})"
            )

        skipped = [task for task in self.tasks if task not in self.schedule]
        if skipped:
            lines.append("Skipped (not enough time left):")
            for task in skipped:
                lines.append(f"- {task.title} ({task.duration_minutes} min, priority: {task.priority})")

        return "\n".join(lines)
