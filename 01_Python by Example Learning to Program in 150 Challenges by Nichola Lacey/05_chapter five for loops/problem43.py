"""
043
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.
"""
while 1 :
    Up_Or_Down = input("Choose your direction [Up of Down ] :")
    Up_Or_Down = Up_Or_Down.lower()
    if Up_Or_Down =="up":
        Top = int(input("Enter a top number that you want to count to : "))
        i = 1
        while i <= Top :
            print(i)
            i+=1
        print("#"*50 + "\n" + "@"*50)

    elif Up_Or_Down == "down":
        number =int(input("Enter a number below 20 : "))
        for i in range(20, number-1, -1):
            print(i)
        print("#"*50 + "\n" + "@"*50)

    else:
        print("I don't understand you ")
        print("#"*50 + "\n" + "@"*50)

