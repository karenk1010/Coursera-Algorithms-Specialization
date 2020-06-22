#!/usr/bin/python3

# Problem Statement #1, #2 {{{
"""
'jobs.txt' file describes a set of jobs with positive and integral weights and
lengths. it has the format:
    [number_of_jobs]
    [job_1_weight][job_1_length]
    [job_2_weight][job_2_length]
    [...][...]

## problem#1
Task is to run the greedy algorithm that schedules jobs in decreasing 
order of the difference (weight-length). If two jobs have equal difference
(weight-length), you shouldschedule the job with higher weight first. 
You should report the sum of weighted completion times of the resulting 
schedule (positive or negative).

## problem#2
Task is to run the greedy algorithm that schedules jobs (optimially) in
decreasing order of the ration (weight/length).
You should report the sum of weighted completion times of the resulting
schedule (positive or negative)

- problem#1 answer: 69119377652
- problem#2 answer: 67311454237
"""
# }}}

