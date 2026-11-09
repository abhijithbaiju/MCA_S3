def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_percentage(total):
    return (total / 300) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

# Main program
m1 = int(input("Enter mark of Subject 1: "))
m2 = int(input("Enter mark of Subject 2: "))
m3 = int(input("Enter mark of Subject 3: "))

total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

print("Total Mark:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
