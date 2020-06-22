#!/usr/bin/python3

# Problem Statement #1, #2 {{{
"""
In this programmingproblem and the next you'll code up the grady algorithms
from lecture for minimzing the weighted sum of completion times.
'jobs.txt' file describes a set of jobs with positive and integral weights and
lengths. it has the format:
    [number_of_jobs]
    [job_1_weight][job_1_length]
    [job_2_weight][job_2_length]
    [...][...]

For example, the third line of the file is "74 59", indicating that the second
job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

## problem#1
Task is to run the greedy algorithm that schedules jobs in decreasing
order of the difference (weight-length). Recall from lecture that this
algorithm is not always optimal.
IMPORTANT: if two jobs have equal difference (weight-length),
you should schedule the job with higher weight first.
BEWARE:if you break ties in a different way, you are likely to get wrong
answer. You should report the sum of weighted completion times of the resulting
schedule (positive or negative).

ADVICE: Ifyou get wrong answer, try out some small test cases to debug your
algorithm.

## problem#2
For this problem, use the same data set as in the previous problem.
Task is to run the greedy algorithm that schedules jobs (optimially) in
decreasing order of the ration (weight/length).
You should report the sum of weighted completion times of the resulting
schedule (positive or negative)

- problem#1 answer: 69119377652
- problem#2 answer: 67311454237
"""
# }}}

# vim:foldmethod=marker:foldlevel=0
