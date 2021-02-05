N, M = [int(i) for i in input().split()]
submissions = [[i for i in input().split()] for _ in range(M)]

#dictionary of the question number as the key and tuple (count of wa attempts, 1 for solved, 0 for unsolved)

question = {}

for submission in submissions:
    question_number, status = submission
    if question_number not in question:
        question[question_number] = [0,0]
    if status == "WA" and question[question_number][1] == 0:
        question[question_number][0] += 1
    else:
        question[question_number][1] = 1

incorrect_amount = 0
correct_amount = 0
for values in question.values():
    if values[1] == 1:
        incorrect_amount += values[0]
    correct_amount += values[1]
print(" ".join([str(correct_amount), str(incorrect_amount)]))

