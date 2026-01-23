student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
counter=len(student_scores)
max=student_scores[0]
for i in range(1,counter):
    if student_scores[i]>max:
        max=student_scores[i]
    else:
        max=max
print(max)
