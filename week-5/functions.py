def get_grades()-> list:
    grades = [];

    while True:
        grade = input("Enter the grade");
        if grade.lower() == 'done':
            break
        grades.append(float(grade));

    return grades


def compute_average(grades: list)-> float:
    return sum(grades) / len(grades);

def main():
    grades = get_grades();
    average = compute_average(grades)
    print(f"The avereage grade is {average:.2f}")

