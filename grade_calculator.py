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