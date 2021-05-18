"""
Ask the user to type in a word and then
display it backwards on separate lines. For
instance, if they type in “Hello” it should
display as shown below:
                        o
                        l
                        l
                        e
                        H
"""
Input = input("Enter a word please : ")
for i in range(1, len(Input)+1):
    print(Input[-i ])
