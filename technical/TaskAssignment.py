def taskAssignment(k, tasks):
    # Write your code here.
    tasks = [(idx, el) for idx, el in enumerate(tasks)]
    tasks.sort(key=lambda item: item[1])

    nTasks = len(tasks)-1
    results = []

    for idx in range(0, k):
        results.append([tasks[idx][0], tasks[nTasks-idx][0]])

    return results

print(taskAssignment(3, [1, 3, 5, 3, 1, 4]) == [[0, 2], [4, 5], [1, 3]])

# task[0] + task[2] = 1 + 5 = 6
# task[4] + task[5] = 1 + 4 = 5
# task[1] + task[3] = 3 + 3 = 6

#Fastest time to complete all task is 6