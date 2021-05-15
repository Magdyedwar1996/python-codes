"""
072
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again
"""
# first way to do it
"""Subjects = ["Arabic","English","Francais","Physics","Chemistry","Mathematics"]
print(Subjects, "\nWhich one of these subjects you don't like : ")
Unliked_one = input()
index = Subjects.index(Unliked_one)
New_list = []
for i in range(6):
    if i != index:
        New_list.append(Subjects[i])
print(New_list)"""

# second way to do it
Subjects = ["Arabic","English","Francais","Physics","Chemistry","Mathematics"]
print(Subjects, "\nWhich one of these subjects you don't like : ")
Unliked_one = input()
index = Subjects.index(Unliked_one)   # to get the index of the unliked one
del Subjects[index] # delete the subject the us er don't like
print(Subjects)