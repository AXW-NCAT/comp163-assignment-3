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
        
git add [username]_assignment_3.py
git commit -m "Pass Test Case 2: Course planning with if/elif/else and comparison operators"

# Decision 2

study_options = ["Programming", "Calculus", "English","History"]
study_choice = input()
if study_choice not in study_options:
    print("Error")
else:
    print("study_choice")
if social_points > 100 or current_gpa < 2.5:
    print("You need to stay in tonight to lock in on school work.")
if social_points < 5 and current_gpa > 3.5:
  print("You may need to get out just a bit more but not too much because your gpa is amazing right now.")
if social_points > 20 and social_points < 75:
  if current_gpa >= 3.2:
    print("You have a great ballance")

# Final Decision
final_gpa = 3.7
community = 21
hours = 20
if stress_level > 100:
    print("You had to drop a class")
    if current_gpa is not final_gpa:
        print("Go to tutoring")
    elif social_points is community:
        print("You've got plenty of friends")
    elif study_hours is hours:
        print("Wow, that's a lot of time")
    else:
        print("IDK")

print(current_gpa)
print(study_hours)
print(social_points)
print(stress_level)






