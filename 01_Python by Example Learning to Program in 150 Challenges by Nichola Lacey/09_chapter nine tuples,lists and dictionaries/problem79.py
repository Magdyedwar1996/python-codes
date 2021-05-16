"""
079
Create an empty list called “nums”.Ask the user to enter numbers. After each number is entered, add
it to the end of the nums list and display the list. Once they have
entered three numbers, ask them if they still want the last number they
entered saved. If they say “no”, remove the last item from the list.
Display the list of numbers.
"""
nums = []
#print(nums)
#print(type(nums))
print("Enter three numbers ")
for i in range(3) :
    number = float(input(f"Number {i } : "))
    nums.append(number)
    print(nums)

ans = input("Do you still want the last number to be saved : ")
if ans == "yes":
    pass
else :
    del nums[2]
    print("The last item was removed according to your choice ")
print(nums)