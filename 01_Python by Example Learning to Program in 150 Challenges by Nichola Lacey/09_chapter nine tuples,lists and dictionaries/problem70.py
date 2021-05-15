"""
070
Add to program 069 to ask the
user to enter a number and
display the country in that
position.
"""
countries = ("Egypt","Saudi Arabia","Libia","America","Germany")
print(countries)
user_choice = input("Choose one of the countries : ")
print(user_choice + " has an index : " , countries.index(user_choice))
position = int(input("Enter an index to get that position in the tuple : "))
print(countries[position])