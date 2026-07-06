from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create an owner
    owner = Owner(name="Jordan", available_time=60)

    # Create at least two pets
    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Luna", species="cat")

    # Connect one pet to the owner for now
    owner.pet = dog

    # Add tasks out of order (mixed times/priorities) so sorting is easier to see
    dog.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high", category="feeding", scheduled_time="07:30"))
    cat.add_task(Task(title="Playtime", duration_minutes=25, priority="low", category="enrichment", scheduled_time="08:00"))
    dog.add_task(Task(title="Morning walk", duration_minutes=20, priority="high", category="exercise", scheduled_time="08:00"))
    cat.add_task(Task(title="Clean litter box", duration_minutes=15, priority="medium", category="cleaning", scheduled_time="09:30"))

    # Mark one task complete
    dog.get_tasks()[0].mark_complete()

    # Combine tasks from both pets
    all_tasks = dog.get_tasks() + cat.get_tasks()

    # Build the schedule
    scheduler = Scheduler(
        tasks=all_tasks,
        available_time=owner.available_time,
        preferences=owner.preferences
    )

    # Print original (unsorted) tasks
    print("Original Tasks")
    print("--------------")
    for task in scheduler.tasks:
        print(task.get_summary())

    # Print tasks sorted by scheduled_time
    scheduler.sort_by_time()
    print("\nTasks Sorted by Scheduled Time")
    print("-------------------------------")
    for task in scheduler.tasks:
        print(f"{task.scheduled_time}: {task.title}")

    # Print incomplete tasks
    print("\nIncomplete Tasks")
    print("-----------------")
    for task in scheduler.filter_by_status(completed=False):
        print(task.get_summary())

    # Print tasks for one pet (Mochi)
    print("\nMochi's Tasks")
    print("-------------")
    for task in scheduler.filter_by_pet_name("Mochi"):
        print(task.get_summary())
    
    # Check for schedule conflicts
    print("\nConflict Check")
    print("--------------")
    print(scheduler.detect_conflicts())

    scheduler.build_schedule()

    # Print today's schedule
    print("\nToday's Schedule")
    print("----------------")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()