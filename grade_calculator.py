print("=== Student Grade Calculator ===")
print("")

student_name = input("Enter stdent name: ")

print("Enter marks out of 100 in each subject")
english = int(input("English marks: "))
math = int(input("Math marks: "))
science = int(input("Science marks: "))

total = english + math + science 
percentage = total / 3

print("")
print("--- Result ---")
print("Student Name:" , student_name)
print("Total Marks:" , total)
print("Percentage:" , percentage)

if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"    
else:
    grade = "Fail"

print("Grade:" , grade)

#Student grade Calculator Improved Version

print("=== Student Grade Calculator ===")
print("")

name = input("Enter student name: ")
student_name = name.title()

print("\nEnter marks out of 100 in each subject")

english = int(input("English: "))
math = int(input("Math: "))
science = int(input("Science: "))
computer = int(input("Computer: "))
urdu = int(input("Urdu: "))

total = english + math +  science + computer + urdu
percentage = total / 5 

print("\n--- Result ---")
print("Student Name  :", student_name)
