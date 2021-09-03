points = 174  # use this input to make your submission
# write your if statement here
if points >= 1 and points <= 50:
    prize_name = "no prize"
    print(f"Congratulations! You won a {prize_name}!".format(prize_name))

    # prize_name = "wooden rabbit"

elif points >= 50 and points <= 150:
   print("Oh dear, no prize this time.")

elif points >= 151 and points <= 180:
    prize_name = "wafer-thin mint"
    print(f"Congratulations! You won a {prize_name}!".format(prize_name))

else:
    prize_name = "penguin"
    print(f"Congratulations! You won a {prize_name}!".format(prize_name))