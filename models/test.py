from operator import itemgetter
# id  joueur, points, classement
student_tuples = [
    [1, 3, 15],
    [6, 1, 12],
    [3, 1, 10],
]
print(student_tuples)

sorted_student = sorted(student_tuples, key=itemgetter(1, 2), reverse=False)
print(sorted_student)
