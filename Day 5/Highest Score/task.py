student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

HighScores = 0
for scores in student_scores:
    if scores > HighScores:
        HighScores = scores

print(HighScores)

#Introduces 'for loops' , we then had the challenge to create code to loop through the scores and pick out the highest score