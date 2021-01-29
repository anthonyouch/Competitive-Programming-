N = int(input())
points = [int(i) for i in input().split()]
new_list = points
while len(new_list) > 2:
    new_lst = []
    for i in range(1, len(new_list),2):
        new_lst.append(max(new_list[i], new_list[i-1]))
    new_list = new_lst


print(points.index(min(new_list))+1)