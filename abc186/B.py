r, c = [int(i) for i in input().split()]
lst = [[int(i) for i in input().split()] for j in range(r)]
# find min of lst
flat_list = []
for sublist in lst:
    for item in sublist:
        flat_list.append(item)

minimum = min(flat_list)

count = 0
for i in flat_list:
    count += (i - minimum)
print(count)