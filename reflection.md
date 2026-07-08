# PawPal+ Project Reflection

## 1. System Design

Before designing the classes, I identified three main actions a user should be able to perform in PawPal+.

First, the user should be able to enter basic owner and pet information. For example, they should be able to add the owner’s name, the pet’s name, and the pet’s species so the app can create a plan for the correct pet.

Second, the user should be able to add pet care tasks. These tasks could include feeding, walking, medication, grooming, or playtime. Each task should include important details like the task name, how long it takes, and how high priority it is.

Third, the user should be able to generate a daily care schedule. The app should look at the available tasks, the time available, and the task priorities, then create a plan that puts the most important tasks first. The schedule should also be easy to understand so the owner knows what to do and why those tasks were chosen.


a. Initial design

For my initial design, I chose four main classes: Owner, Pet, Task, and Scheduler. I chose these because they matched the main parts of the PawPal+ app: a pet owner, their pet, the care tasks they need to do, and the scheduling logic that organizes those tasks.

The Owner class is responsible for storing information about the person using the app, such as their name, available time, and preferences. The Pet class represents the pet being cared for and stores details like the pet’s name, species, and list of tasks. The Task class represents one care activity, such as feeding, walking, medication, grooming, or playtime. Each task needs information like a title, duration, priority, category, and whether it is completed.

The Scheduler class is responsible for the planning part of the app. Its job is to take the available tasks, look at the available time, sort or prioritize the tasks, and build a daily care plan. I wanted to keep the scheduler separate from the task and pet classes because scheduling is the main logic of the app, while the other classes mostly store information.


**b. Design changes**

After reviewing my class skeleton with Claude Code, I noticed that a few relationships from my UML were not fully represented in the Python code yet. My UML showed that an Owner owns a Pet, but my first version of the Owner class did not actually store a pet reference. I also realized that the scheduler would eventually need access to owner preferences, since preferences are part of the constraints for building a useful daily plan.

Based on that feedback, I made three small design updates. I added a pet attribute to Owner, a preferences value to Scheduler, and a scheduled_time field to Task so the schedule can later show when each task is planned. I did not implement the full scheduling logic yet because this phase was mainly about making sure the class skeleton matched the UML and project requirements. These changes made the design feel more complete before moving on to the actual scheduler implementation.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler mainly considers available time, task priority, scheduled time, completion status, pet name, and whether a task is recurring. The most important constraint is available time because the schedule should not include more care tasks than the owner can realistically complete in one day. Priority is also important because tasks like feeding, medication, or walks should usually happen before lower-priority tasks like extra playtime.

I decided that time and priority mattered most because they directly affect whether the daily plan is useful. If the owner only has 60 minutes, the scheduler should fit the most important tasks into that time instead of just listing everything. Later, I also added scheduled time, filtering, recurrence, and conflict detection so the app could feel more like a real pet care planning tool instead of only a basic task list.

**b. Tradeoffs**

One tradeoff my scheduler makes is that the conflict detection is simple. It checks whether two tasks have the exact same scheduled_time, but it does not fully calculate whether task durations overlap. For example, if one task starts at 08:00 and takes 30 minutes, and another task starts at 08:15, a real calendar would treat that as a conflict, but my current version would not catch it unless the start times match exactly.

I think this tradeoff is reasonable for this project because PawPal+ is still a beginner-level scheduling app, and exact-time conflict detection is easier to understand and test. It still gives the user a useful warning when two tasks are clearly scheduled at the same time, without making the algorithm too complicated. If I had more time, I would improve this by converting scheduled times into minutes and checking whether the full time ranges overlap.

---

## 3. AI Collaboration

**a. How you used AI**

I used Claude Code during several parts of the project, but I tried to use it more like a teammate instead of just letting it write everything at once. In the design phase, I asked it to help turn my ideas into a Mermaid UML diagram with the four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. That helped me see the system structure before writing the code.

I also used AI to review my class skeleton before implementation. Claude pointed out that my first version was missing some relationships from the UML, like the `Owner` needing a `pet` attribute and the `Scheduler` needing access to preferences. That feedback helped me make small design changes before the code got too complicated.

During the algorithm phase, I used AI to brainstorm realistic improvements like sorting by scheduled time, filtering by status or pet name, recurring tasks, and conflict detection. The most helpful prompts were the ones where I asked for one small change at a time and told Claude exactly what not to change. That made the suggestions easier to review and kept the project from becoming too complicated.


**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was when Claude reviewed my `detect_conflicts()` method. It said that using `defaultdict` would be a slightly more Pythonic way to group tasks by scheduled time, but it also explained that my current version was already clear and readable. I decided to keep my existing version because it was easier for me to understand and did not require another import.

I verified AI suggestions by reading the diff before accepting changes, running the app or CLI demo, and running pytest. For example, after adding the automated tests, I ran `python -m pytest tests/test_pawpal.py`, and all 5 tests passed. This helped me make sure the AI-generated changes actually worked instead of just assuming they were correct.


---


## 4. Testing and Verification

**a. What you tested**

I tested the most important backend behaviors in `pawpal_system.py`. First, I tested that a task can be marked complete, because completion status is one of the basic pieces of task management. Second, I tested that adding a task to a pet actually stores the task in the pet’s task list, since the rest of the scheduler depends on tasks being saved correctly.

I also tested the smarter scheduling features. I tested sorting by scheduled time to make sure tasks can be placed in chronological order. I tested recurring task logic by checking that a daily task creates a new task for the following day. I also tested conflict detection by creating two tasks with the same scheduled time and confirming that the scheduler returns a conflict warning.

These tests were important because they checked both the basic class behavior and the algorithmic features I added later. They helped prove that the project was not only displaying a UI, but that the backend logic was actually working.


**b. Confidence**

I would rate my confidence in the system as 4 out of 5 stars. I feel confident because my automated tests passed, including tests for task completion, adding tasks to a pet, sorting by time, recurring tasks, and conflict detection. I also manually tested the CLI demo and Streamlit app to confirm that the scheduler output was readable.

I am not giving it a full 5 stars because the scheduler still makes some simplifying assumptions. For example, conflict detection only checks if two tasks have the exact same scheduled time. It does not yet check if one task from 08:00 to 08:30 overlaps with another task starting at 08:15. If I had more time, I would test and improve full time-range overlap detection, multiple pets in the UI, and more recurrence cases like weekly tasks with missing due dates.


---


## 5. Reflection

**a. What went well**

The part I am most satisfied with is that the project grew from a simple UML diagram into a working system with classes, scheduling logic, a CLI demo, a Streamlit UI, and automated tests. I liked that the `Task`, `Pet`, `Owner`, and `Scheduler` classes stayed separated because it made the code easier to understand. I also liked that the scheduler became smarter over time with sorting, filtering, recurring tasks, and conflict detection.


**b. What you would improve**

If I had another iteration, I would improve the scheduling logic so conflict detection checks overlapping time ranges instead of only exact matching start times. I would also improve the UI so the user can manage multiple pets more clearly, mark tasks complete from the Streamlit app, and choose recurrence options directly in the form. Right now, some of the smarter backend features exist in the logic layer, but the UI could still make them easier for a normal user to control.

**c. Key takeaway**

The biggest thing I learned is that using AI does not remove the need to understand the system design. I still had to act like the lead architect by deciding which classes made sense, which suggestions to accept, what to test, and when to keep the code simple. AI was helpful for brainstorming, reviewing, and generating small pieces of code, but I had to guide it carefully and verify the final result myself.

