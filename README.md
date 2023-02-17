# print_jobs_simulator
a Printing simulation using a Queue

Question::

Consider the following situation in a computer science laboratory. On any average day about
10 students are working in the lab at any given hour. These students typically print up to twice
during that time, and the length of these tasks ranges from 1 to 20 pages. The printer in the
lab is older, capable of processing 10 pages per minute of draft quality. The printer could be
switched to give better quality, but then it would produce only five pages per minute. The
slower printing speed could make students wait too long. What page rate should be used?

Assumptions::

As students submit
printing tasks, we will add them to a waiting list, a queue of print tasks attached to the printer.
When the printer completes a task, it will look at the queue to see if there are any remaining
tasks to process. Of interest for us is the average amount of time students will wait for their
papers to be printed. This is equal to the average amount of time a task waits in the queue.
To model this situation we need to use some probabilities. For example, students may print
a paper from 1 to 20 pages in length. If each length from 1 to 20 is equally likely, the actual
length for a print task can be simulated by using a random number between 1 and 20 inclusive.
This means that there is equal chance of any length from 1 to 20 appearing.
If there are 10 students in the lab and each prints twice, then there are 20 print tasks per hour
on average. What is the chance that at any given second, a print task is going to be created?
The way to answer this is to consider the ratio of tasks to time. Twenty tasks per hour means
that on average there will be one task every 180 seconds:

(10 students * 2 / 1 Hour) * 1/ 60 mins * 1/60 seconds = 20 / 3600 -> 1 task per 180 mins

By use of a random number, we can ensure that whenever 180 is produced by the random number generator, a task is generated.

Pseudo Code::
1.Create a Queue for the printing tasks and a list to hold waiting times of the tasks
2. For each second:
3.     if new task created then:
4.         Get task timestamp
5.         add task to the Queue
6.     if the printer is idle and the stack is not empty:
7.         Get next task from Queue
8.         compute task waiting time(task timestamp - current time)
9.         send task to printer
10.    compute time taken by task
11.  average waiting time = summation of tasks average time divided by the length of the list
12.  compute remaining tasks in the Queue
13.  Output the average waiting time and the remaining tasks.
14.

***This task is created from the book:: Problem Solving with Algorithms and
Data Structures
Release 3.0 by Brad Miller, David Ranum***
