N, C = [int(i) for i in input().split()]
contents = [[int(i) for i in input().split()] for i in range(N)]

sorted_contents = contents

intervals = {}

for services in sorted_contents:
    if services[0] not in intervals:
        intervals[services[0]] = 0

    intervals[services[0]] += services[2]

    if services[1] + 1 not in intervals:
        intervals[services[1] + 1] = 0

    intervals[services[1]+1] -= services[2]

intervals_list = []

for key, value in intervals.items():
    temp = [key,value]
    intervals_list.append(temp)


sorted_intervals = sorted(intervals_list, key=lambda x: x[0])

total = 0
current_cost = 0
for interval_index in range(len(sorted_intervals) - 1):

    current_cost +=  sorted_intervals[interval_index][1]

    interval_length = (sorted_intervals[interval_index +1][0] - sorted_intervals[interval_index][0])

    if current_cost * interval_length <= C * interval_length:
        total += current_cost * interval_length
    else:
        total += C * interval_length

print(total)


