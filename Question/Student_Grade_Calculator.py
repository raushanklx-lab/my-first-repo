# 1. Mini Project: Student Grade Calculator

# Create a program that:
# Takes marks of 5 subjects
# Calculates total, percentage
# Assigns a grade  # 80% Grade A,  60% Grade B, 40% Grade C, 33% Grade D, below 33% Grade E

Marks = []
for i in range(1,6):
    Mark = int(input(f"Enter Marks of Subject {i} :"))
    Marks.append(Mark)

total = sum(Marks)
percentage = (total / 500) * 100

if percentage >= 80:
    Grade = "A"
elif percentage >= 60:
    Grade = "B"
elif percentage >= 40:
    Grade = "C"
elif percentage >= 33:
    Grade = "D"
else:
    Grade = "E"

print("\nTotal Marks : ",total )
print("\nPercentage : ",percentage )
print("\nGrade : ", Grade)