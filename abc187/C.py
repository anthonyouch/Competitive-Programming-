N = int(input())
inputs = [input() for i in range(N)]

exclam_inputs = set([str[1:] for str in inputs if str[0] == "!"])
non_exclam_inputs = [str for str in inputs if str[0] != "!"]

for word in non_exclam_inputs:
    if word in exclam_inputs:
        print(word)
        exit()
else:
    print('satisfiable')

