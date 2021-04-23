try :
    print("magdy loves programming ")

except :
    print("AN ERROR OCCURED !")



while True:
    try :
        num1 = float(input("enter num1 :"))
        num2 = float(input("enter num2 :"))
        div  = num1 / num2
        print(div)
    except ( ZeroDivisionError , ValueError ) :
            print("an error occured : ZeroDivisionError ")
    except :
            print("an unusal error occured ")




























