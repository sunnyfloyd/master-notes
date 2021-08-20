# Scrum

## Sources

- [Scrum Fundamentals (O'Reilly)](https://learning.oreilly.com/videos/scrum-fundamentals/9780133749076/).

## Scrum Fundamentals

### Waterfall

- Analysis -> Design -> Develop -> Test -> Deploy

- All steps are done sequentially. If any changes/features have not been foreseen at the earlier stages, but later ones included them, previous stages need to be revisited and adjusted.

- Waterfall methodology relies on a formal plan with milestones. This plan is often a guess. If any stage takes longer than initially planned, the whole plan needs to change.

- Each stage is often done in isolation - there is no exchange of the information between phases.

- In Scrum methodology - all of the stages overlap each other.

### Agile Manifesto

1. Individuals and itneractions > Processes and tools
2. Working software > Comprehensive documentation
3. Customer collaboration > Contract negotation
4. Responding to change > Following a plan

### Agile Concepts

1. Short feedback loops
2. Just in time requiremnets and design
3. Delivering incremental value
4. Release ready deliverables (complete code, tested, integrated, documented, deployed)
5. Sustainable pace
6. Lean management hierarchy (not too many decision people)
7. Self-organizing teams (people can organize and manage themselves without unnecassary supervision - this will empower people)
8. Trust, courage and transparency balance
9. Continous delivery (idea that something can be taken from coding to deployment as fast as possible)
10. Embracing change
11. Inspect and adapt

### Scrum Overview

#### Roles

- Product owner:
  - maximizes product value
  - manages the product backlog
  - represents the users
  - single person

- Scrum Master:
  - shepard of Scrum
  - servant leader
  - removes impediments
  - resolves conflicts

- Development team:
  - cross functional
  - self organizing
  - highly collaborative
  - 5 - 9 members

#### Artifacts

- Product vision:
  - target market
  - business need/opportunity
  - key features
  - value to the company

- Product backlog:
  - single source of requirements
  - constantly evolving
  - ordered based on value
  - estimated by the development team

- Release plan:
  - forecast based on empirical data
  - overlay on the product backlog
  - updated every Sprint

- Sprint backlog:
  - product backlog items for a Sprint
  - plan to deliver a product increment
  - owned by the development team
  - dynamic and highly visible

- Burndown chart:
  - tracks work remaining by day
  - updated by the development team
  - displayed prominently

- Impediment list:
  - blocking or affecting performance
  - updated by the Scrum team
  - monitored by the Scrum Master

#### Events

- Sprint planning:
  - determines what will be delivered
  - past performance/capacity
  - determine how it will be delivered
  - create Sprint backlog

- The Sprint:
  - time boxed to one month or less
  - clearly stated Sprint goal
  - potentially releasable increment
  - scope set by a Scrum team

- Daily Scrum:
  - time boxed to 15 minutes
  - inspect work done yesterday
  - plan work for today
  - identify possible impediments

- Product backlog grooming:
  - clarifying and estimating new items
  - reviewing higher priority items
  - less detail on lower priority items
  - around 10% of the Sprint

- Sprint review:
  - demo product increment
  - elicit feedback from stakeholders
  - plan what to do next
  - review the release plan

- Sprint retrospective:
  - Scrum team inspect and adapt
  - what went well?
  - what can we do better?
  - plan for improvements

### Starting a Scrum Project

#### Sprint Zero (not recommended)

- Product vision
- Initial product backlog
- Initial release plan
- Architecture approach and coding practices
- Continous integration environment
- Small product increment

#### Creating a Product Vision

- Creating a product vision:
  - target market
  - business need/opportunity
  - key features
  - value to the company

- Qualities of a product vision:
  - broad and inspiring
  - clear and stable
  - short and sweet
  - highly visible
  - frequently revisited

#### Creating Initial Product Backlog

- Creating Initial Product Backlog
  - single source of requirements
  - constantly evolving
  - ordered based on value
  - estimated by the development team

- What goes on to the product backlog:
  - user requirements
  - technical requirements
  - bugs

#### User Stories

- short and simple
- user perspective
- focus on discussions

- Conditions of satisfaction:
  - required for acceptance
  - represent tests
  - specifc not details

- Conditions of good user stories:
  - independent
  - negotiable
  - valuable
  - estimable
  - small
  - testable

- Splitting user stories
  - theme
  - epic
  - user story (something that is small enough to fit into sprint)

#### Roles and Personas

- Think about actual customers when building a project.

#### Prioritizing Product Backlog

- Business value (increase revenue, reduce cost, attract new customers, retain customers)
- ROI (value/effort)
- Feature grouping
- Politics

- When prioritizing user stories 100 points can be assigned among all of the user stories to determine their priority level. Other method would be to assign score from 1 - 100 (additional meaning can be assigned to arbitraty ranges like: 90 - 100 -> customer will lose market share if not implemented)

#### Agile Estimation

- Story points
  - high level estimate of size (effort)
  - based on relative scale
  - estimated as a team
  - not based on duration
  - can use Fibonacci sequence for assigning story points - to get some reference point, well understood example by team members should be discussed and assigned story points
  - can use *planning poker* to assign points - if there is a large dispersion in points, more discussion is needed

#### Creating a Release Plan

- Determine a velocity (in story points as a unit) which is equal to historical amount of work that can be accomplished in a given time.

- To determine a velocity for a new team just discuss stories from product backlog and make a collective assumption how many stories, hence story points, this new team thinks it can complete in a given timeframe.

- Plan using the worst case scenario.

### Executing the Sprint

#### Holding the Sprint Planning Meeting

- Identify the sprint goal

- Create the **sprint backlog** - plan what work from the product backlog will be a target for a given sprint taking into consideration team's velocity.

- Backlog item chosen to be a part of a sprint should be discussed and broke into smaller tasks with time estimate for each task.

- Sprint backlog should be created with **SMART** technique (specific, measurable, achievable, relevant, time boxed).

- When deciding on commiting to a story - **fist of five** can be used. Number of fingers determine how much given person agrees/disagrees with current version of a story.

#### Working As a Scrum Team

- Limit work in progress - all team members should align with capacity of other people in the flow so that it is not disturbed (for example one person in the flow ends up with too much work that cannot be completed within the sprint).

#### Holding the Daily Scrum

- Daily Scrum meeting is strictly for planning for the development team. Other stakeholders may join such meeting, but this meeting should not be a status reporting for them.

- Same time and place.

- 15 minutes or less.

- Planning meeting, not a status meeting. This is what I am working on, and this is what I am held with - team discusses how to address this.

- Inspect progress - tell more about the task that you are currently on/just completed. Were there any issues? Are there any new tasks coming up that you did not expect?

  - What did you do yesterday?
  - What are you going to do today?
  - Any impediments?

- Use task board to visualize the progress with user stories (table with user stories and current progress in columns - not done, in progress, done, blocked).

- Use chart representing working hours remaining with a trendline providing information about the estimated time. Use sticky notes to explain bumps in the actual progress line (f.e. more tasks have been identified).

- Similar chart should be used to represent actual tasks (product backlog items) being completed. No trend line for this chart though.

#### Agile Engineering Practices

- Focus on new features and not frameworks - frameworks are not something that can be presented to the user.

- **YAGNI Principle** (You Ain't Gonna Need It) - focus on implementing the actual feature - do not try to make it overly robust or future-resilent. Concentrate on what is needed now and not gold plating.

##### Continous Integration

- Completed part of the code should be deployed as soon as possible and integrated with all the others newly deployed features.

- If newly integrated code makes the build fail, fixing the issues should be the top priority.

- **Test Driven Development** allows to develop in a fashion that starts from the perspective of a user and builds down to the backend features that support actual user needs/functionalities.

- **Automated Testing**:

  - Unit Tests - verify whether single module works as expected;
  - Integration Tests - verify whether modules work properly together;
  - Feature Tests - tests from the user perspective that focus on UI.

- Clear definition of task/work being done: features, tests, deployment, documentation.

#### Quality Assurance in Agile

- Start with developing tests, and after initial tests are created start developing a feature. Then test and code iteratively. After code freeze perform regression and integreation testing.

- QA Best Practices:

  - hire good quality QA engineers,
  - QA and dev sit together,
  - QA is involved in analysis and design,
  - Test as you go,
  - Make testing part of a definition of done,
  - Limit work in progress,
  - Everyone can help test,
  - Frequent, incremental releases for feedback,
  - Set bug queue limits.

- When bug is being found task for fixing this bug should be created and assigned to a developer, and test cases should be written to ensure that this bug will not escape.

- Dealing with bugs:

  - critical bugs
  - non-critical bugs
  - enhancements (those are not bugs - those are new product backlog items).

### Ending the Sprint

#### Sprint Review

- All of the stakeholders should be present.

- Less than 2 hours meeting

- Holding the sprint review:

  - demo what is *done*
  - review what wasn't done
  - review progress
  - discuss next steps.

#### Delivering a Product Increment

- Potentially shippable.

- Delivery is a non event.

- Hardening sprint - it is mainly about testing, and, in case of critical bugs, fixing them.

#### Sprint Retrospective

- Holding the sprint retrospective:

  - audience: product owner, development team, scrum master
  - equal voice
  - focus on improvement
  - prioritize (voting)
  - take real action.

- Take a table with two columns: 'what went well?' and 'what could be better?'. And ask people to write their opinions down in 10 minutes. Scrum master then reads them out loud and clarifies if needed and adds these suggestions to the columns grouping similar topics. Team then places poker chips on each item to identify which one should be discussed further.
