student_Dictionary = {"alice":85,"john":77,"joe":90,"rohan":69}
student_Name = input("Enter the student's name: ")
try:
    print(student_Name, "'s marks: ", student_Dictionary[student_Name])
except KeyError:
    print("Student not found")