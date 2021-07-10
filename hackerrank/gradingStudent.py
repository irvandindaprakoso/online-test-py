def gradingStudents(grades):
    for i in range(n):
        if grades[i] >=38 and grades[i]%5 > 2:
            grades[i] = grades[i]+ (5-(grades[i]%5))
    return grades
