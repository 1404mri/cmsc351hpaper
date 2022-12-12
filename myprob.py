
class Node:
    def __init__(self, val):
        self.val = val

def time_soln(time_diffs):
    x = 0
    task_times = [0] * len(time_diffs)
    for i in range(len(time_diffs) - 1, -1, -1):
         task_times[i] = time_diffs[i]
         if (i < len(time_diffs) - 1 and task_times[i] > task_times[i + 1]):
             task_times[i + 1] += (time_diffs[i] - task_times[i + 1])/2.0
             task_times[i] = task_times[i + 1]
    print(task_times)
