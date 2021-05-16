"""
080
Ask the user to enter their first name and then display
the length of their first name. Then ask for their surname
and display the length of their surname. Join their first
name and surname together with a space between and
display the result. Finally, display the length of their full
name (including the space).V
"""
name = input("Enter your name please : ")
print("The length of your name is ",len(name))

sur_name = input("Enter your name please : ")
print("The length of your name is ",len(sur_name))
Entire_name = name +" "+ sur_name
print(Entire_name)
print("The length of the whole name is : ",len(Entire_name))
