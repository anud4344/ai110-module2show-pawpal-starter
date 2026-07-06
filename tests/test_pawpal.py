from datetime import date, timedelta

from pawpal_system import Task, Pet, Scheduler


def test_task_completion():
    task = Task(title="Morning walk", duration_minutes=20, priority="high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet(name="Mochi", species="dog")
    task = Task(title="Feeding", duration_minutes=10, priority="high")

    assert len(pet.get_tasks()) == 0

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1
    assert pet.get_tasks()[0] is task


def test_sort_by_time_orders_tasks_chronologically():
    task_afternoon = Task(title="Evening walk", duration_minutes=20, priority="high", scheduled_time="14:00")
    task_morning = Task(title="Breakfast", duration_minutes=10, priority="high", scheduled_time="08:00")
    task_midmorning = Task(title="Playtime", duration_minutes=15, priority="low", scheduled_time="09:30")

    scheduler = Scheduler(tasks=[task_afternoon, task_morning, task_midmorning])

    scheduler.sort_by_time()

    scheduled_times = [task.scheduled_time for task in scheduler.tasks]
    assert scheduled_times == ["08:00", "09:30", "14:00"]


def test_create_next_occurrence_for_daily_task():
    original_due_date = date(2026, 1, 1)
    task = Task(
        title="Give medication",
        duration_minutes=5,
        priority="high",
        frequency="daily",
        due_date=original_due_date,
    )

    next_task = task.create_next_occurrence()

    assert next_task is not None
    assert next_task.title == task.title
    assert next_task.frequency == task.frequency
    assert next_task.due_date == original_due_date + timedelta(days=1)
    assert next_task.completed is False


def test_detect_conflicts_finds_shared_scheduled_time():
    task_one = Task(title="Morning walk", duration_minutes=20, priority="high", scheduled_time="08:00")
    task_two = Task(title="Feeding", duration_minutes=10, priority="high", scheduled_time="08:00")

    scheduler = Scheduler(tasks=[task_one, task_two])

    conflict_message = scheduler.detect_conflicts()

    assert "Conflict" in conflict_message
    assert "08:00" in conflict_message
