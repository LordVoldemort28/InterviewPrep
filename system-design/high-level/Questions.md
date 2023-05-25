Design Task Scheduler
-----------------------
More info on the probelm

User should be able to see the Jobs in UI and do CRUD operations.
Jobs can be of 2 types.
Single Execution (executed once, may be in some time in future.
Repetitive ( can be executed multiple times based on the schedule given)
Have to handle 10 Million Jobs a day.
If Job execution fails , retry the job for 5 times before giving up.
More specific questions

What would be your DB schema for this?
How will you store the jobs and execute it at the given time? Will you do a constant poll? if so, what is the time interval?
Do we have any other approach apart from polling the DB constantly?
How many machine are needed to handle 10Million Jobs/Day.

https://leetcode.com/discuss/interview-question/system-design/344524/Amazon-or-Design-a-JobTask-Scheduler