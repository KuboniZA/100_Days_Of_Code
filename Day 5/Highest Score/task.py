
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(student_scores[0, 10]))

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

lowest_score = 10000000
for score in student_scores:
    if score < lowest_score:
        lowest_score = score

middle_score = 0

# for score in student_scores:
#     if score > highest_score and score < lowest_score:
#         middle_score = score

print(f"The highest score is {highest_score} and the lowest score {lowest_score}. The score in the middle is {middle_score}.")
