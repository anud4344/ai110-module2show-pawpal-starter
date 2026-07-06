from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create an owner
    owner = Owner(name="Jordan", available_time=60)

    # Create at least two pets
    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Luna", species="cat")

    # Connect one pet to the owner for now
    owner.pet = dog

    # Add tasks with different times and priorities
    dog.add_task(Task(title="Morning walk", duration_minutes=20, priority="high", category="exercise"))
    dog.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high", category="feeding"))
    cat.add_task(Task(title="Clean litter box", duration_minutes=15, priority="medium", category="cleaning"))
    cat.add_task(Task(title="Playtime", duration_minutes=25, priority="low", category="enrichment"))

    # Combine tasks from both pets
    all_tasks = dog.get_tasks() + cat.get_tasks()

    # Build the schedule
    scheduler = Scheduler(
        tasks=all_tasks,
        available_time=owner.available_time,
        preferences=owner.preferences
    )

    scheduler.build_schedule()

    # Print today's schedule
    print("Today's Schedule")
    print("----------------")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()