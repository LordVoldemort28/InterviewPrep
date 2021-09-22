def merge_meeting(meetings):

    merged_meeting = []
    meetings.sort()

    start_time, end_time = meetings.pop(0)
    min_start = start_time
    max_end = end_time

    while meetings:

        start_time, end_time = meetings.pop(0)

        if max_end >= start_time:
            max_end = max(max_end, end_time)
            min_start = min(min_start, start_time)
        else:
            merged_meeting.append((min_start, max_end))
            min_start, max_end = start_time, end_time

    merged_meeting.append((min_start, max_end))

    return merged_meeting


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
result = [(0, 1), (3, 8), (9, 12)]

print(merge_meeting(meetings))
