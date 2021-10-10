names =  input("Enter names seperated by commas : ").split(",")
assignments = [int(x) for x in input("Enter assignment counts separated by commas : ").split(",")]
grades = [int(y) for y in input("Enter grades separated by commas : ").split(",")]
new_grades = []
for i in range(len(assignments)):
    new_grades.append(grades[i] + 2 * assignments[i])

#print(new_grades)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(assignments)) : 
    print(message.fomate(names[i],assignments[i],grades[i],new_grades[i])
    
    
        