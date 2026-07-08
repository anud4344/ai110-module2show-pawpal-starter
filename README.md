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

## ✨ Features

**Owner & pet setup**
The Streamlit app lets you enter an owner's name and available time, plus a pet's name and species. These are stored as real `Owner` and `Pet` objects (`app.py`) that persist across reruns using `st.session_state`.

**Adding tasks**
Each task captures a title, duration, priority, and scheduled time. Under the hood this creates a `Task` object and adds it to the pet's task list via `Pet.add_task()`, which also stamps the task with the pet's name so it can be filtered later.

**Building a daily schedule**
`Scheduler.build_schedule()` takes all of a pet's tasks and fits as many as it can into the owner's available time, always favoring higher-priority tasks first. Tasks that don't fit are left out and reported separately rather than silently dropped.

**Priority and time sorting**
`Scheduler.sort_tasks()` orders tasks high → medium → low priority. `Scheduler.sort_by_time()` orders them chronologically by `scheduled_time`, with unscheduled tasks pushed to the end — handy for reviewing the day's plan at a glance.

**Filtering**
`Scheduler.filter_by_status()` splits tasks into completed vs. incomplete, and `Scheduler.filter_by_pet_name()` narrows the list down to one pet — useful once a household has more than one animal to track.

**Conflict detection**
`Scheduler.detect_conflicts()` scans for tasks that share the exact same `scheduled_time` and returns a warning message naming the conflicting tasks, instead of letting them silently overlap.

**Daily & weekly recurring tasks**
Tasks can be marked `frequency="daily"` or `"weekly"`. Calling `Task.create_next_occurrence()` generates the next task instance with the due date pushed forward by 1 day or 7 days. One-off tasks (`frequency="once"`) simply return `None` — they don't recur.

**Schedule results in the UI**
The Streamlit app surfaces all of this directly: it shows the current task table, flags conflicts with a warning banner, displays the time-sorted list, and prints the full explained plan (including anything skipped) via `Scheduler.explain_plan()`.

**Automated tests**
Run `python -m pytest` to verify the core logic — task completion, adding tasks to a pet, sorting by scheduled time, daily recurrence, and conflict detection all have dedicated tests in `tests/test_pawpal.py`.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
