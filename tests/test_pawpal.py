from pawpal_system import Task, Pet


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
