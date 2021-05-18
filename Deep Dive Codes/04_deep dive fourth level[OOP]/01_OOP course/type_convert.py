global userinput

def readinput():
    userinput = input("Enter a number Please : ")
    return userinput
def temp_convert(var):
    try:
        return int(var)
    except:
        print("The argument dose't contain numbers !")
        execept_input = readinput()
        userinput = temp_convert(execept_input)

userinput =readinput()
temp_convert(userinput)
print(userinput)
