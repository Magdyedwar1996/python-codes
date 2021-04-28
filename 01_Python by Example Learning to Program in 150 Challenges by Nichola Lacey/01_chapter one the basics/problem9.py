"""
009
Write a program that will ask for a
number of days and then will
show how many hours, minutes
and seconds are in that number of
days.
"""
Number_of_Days = int(input("Enter the number of days :"))
Number_of_Hours = Number_of_Days * 24
Number_of_Minutes = Number_of_Hours * 60
Number_of_Seconds= Number_of_Minutes * 60

print(f"""there are {Number_of_Hours} hours , \
and {Number_of_Minutes} minutes and {Number_of_Seconds} seonds """)

