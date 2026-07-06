# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule 
---------------- 
Daily plan: 
- 0 min: Morning walk (20 min, priority: high) 
- 20 min: Breakfast feeding (10 min, priority: high) 
- 30 min: Clean litter box (15 min, priority: medium) Skipped (not enough time left):
- Playtime (25 min, priority: low)
```
## 🧪 Testing PawPal+

To run the automated tests, use:

```bash
python -m pytest
```

The test suite checks the main backend behavior in `pawpal_system.py`. The tests verify that a task can be marked complete, that adding a task to a pet stores it in the pet's task list, that tasks can be sorted by scheduled time, that a daily recurring task creates a next occurrence for the following day, and that the scheduler can detect conflicts when two tasks have the same scheduled time.

Sample test output:

```text
# Run this command in the terminal:
# python -m pytest

# Example passing result:
# 5 passed in 0.03s 100% passed
```

**Confidence Level: 4/5 stars**

I would rate my system reliability as 4 out of 5 stars. The automated tests passed, including tests for task completion, adding tasks to a pet, sorting by scheduled time, recurring task creation, and conflict detection. I am not giving it a full 5 stars because the app still has some simple scheduling assumptions, like detecting exact time matches instead of full overlapping time ranges.

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_tasks()` and `Scheduler.sort_by_time()` | Sorts tasks by priority first, and can also sort tasks by scheduled time so the plan is easier to read. |
| Filtering | `Scheduler.filter_by_status()` and `Scheduler.filter_by_pet_name()` | Filters tasks by completion status or pet name, so the owner can see only incomplete tasks or tasks for one specific pet. |
| Conflict handling | `Scheduler.detect_conflicts()` | Checks if two or more tasks have the same scheduled time and returns a warning message instead of crashing. |
| Recurring tasks | `Task.create_next_occurrence()` | Creates a new task for the next day or next week when a daily or weekly task repeats. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
