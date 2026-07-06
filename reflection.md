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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff my scheduler makes is that the conflict detection is simple. It checks whether two tasks have the exact same scheduled_time, but it does not fully calculate whether task durations overlap. For example, if one task starts at 08:00 and takes 30 minutes, and another task starts at 08:15, a real calendar would treat that as a conflict, but my current version would not catch it unless the start times match exactly.

I think this tradeoff is reasonable for this project because PawPal+ is still a beginner-level scheduling app, and exact-time conflict detection is easier to understand and test. It still gives the user a useful warning when two tasks are clearly scheduled at the same time, without making the algorithm too complicated. If I had more time, I would improve this by converting scheduled times into minutes and checking whether the full time ranges overlap.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
