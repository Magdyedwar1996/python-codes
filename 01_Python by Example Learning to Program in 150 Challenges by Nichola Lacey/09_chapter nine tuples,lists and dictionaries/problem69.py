"""
069
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple
"""
countries = ("Egypt","Saudi Arabia","Libia","America","Germany")
print(countries)
user_choice = input("Choose one of the countries : ")
print(user_choice + " has an index : " , countries.index(user_choice))