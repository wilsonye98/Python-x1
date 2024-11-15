# Given the participants score sheet for your University Sports Day, you are
# required to find the runner-up score. You are given scores. Store them in a
# list and find the score of the runner-up.

def runner_up(scores):
    lst = set(scores.split(' '))
    runner = sorted(lst)[-2]
    return runner

print(runner_up('2 3 6 6 5'))