student_name = "Aaron Williams"
current_gpa = 3.0
study_hours = 2
social_points = 25
stress_level = 70

print("Welcome Aaron!!: ")
print(student_name)
print(current_gpa)
print(study_hours)
print(social_points)
print(stress_level)


git add [username]_assignment_3.py
git commit -m "Pass Test Case 1: Initial game setup with required variables"

# Decision 1
print("A) Light (12 credits)")
print("b) Standard (15 credits)")
print("c) Heavy (18 credits)")
input = ("Choose your cource laod: ")

if input == "A":
  if current_gpa >= 3.5:
    print("Light Load")
  else:
    stress_level += 12
elif input == "B":
  if current_gpa >= 3.0:
    print("Standard")
  else:
    social_points - 10
elif input == "C":
  if current_gpa >= 2.5:
    print("Heavy Load")
  else:
    study_hours += 20
else:
  print("Please choose another option")
        
  





