""" creating an Admission program to calculate the aggregate score,
and tell the students the faculty and department he or she is likely
to be admitted

Criteria for Admission
0-49 No Admission
50-54 Agric Department
55-60 Botany and Zoology Department
61-70 Computer Science,physiology and Stat
71-74 Banking & Fin, Acct and Insurance
80 and Above Medicine and Law
"""

def performance():
    aggregate = []
    while True:
        student_score = input("what is your aggregate --> ")
        if student_score == "q":
            break
        aggregate.append(int(student_score))
    dept_faculty = student_faculty_dept(aggregate)
    if dept_faculty.startswith("No Admission"): print("No Admission given")
    print(f"You have been offered Admission in this Institution into either {dept_faculty}")


def student_faculty_dept(accept_list: list):
    sum_score = sum(accept_list)
    if 0 < sum_score <= 49:
        return "No Admission"
    elif 49 < sum_score <= 54:
        return "Agric Department"
    elif 54 < sum_score <= 60:
        return "Botany and Zoology"
    elif 60 < sum_score <= 70:
        return "Computer Science, Psycology and Statistics"
    elif 70 < sum_score <=74:
        return "Pharmacy, Pysiology and Nursing"
    elif 74 < sum_score <=80:
        return "Banking & finance, Accounting and Insurance"
    elif  sum_score >= 80:
        return "Medcine and Law"
    else:
        None


if __name__== "__main__":
    performance()
