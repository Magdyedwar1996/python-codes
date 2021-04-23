"""while True :
    try :
        #print("magdy likes his career")
        num = int(input("enter a num : "))
        a = int(input("enter a num : "))
        out = num / a
        print(out)
    except ZeroDivisionError:
        print("an error occured  : ZeroDividionError")
    except ValueError :
        print("an error occured : ValueError ")"""

"""
try :
    rt = [1,2,3]
    print(rt)
    rt[2] = 8
    print(rt)
    rt.append([2,5,4])
    print(rt)
    print(rt[6])
except IndexError as er :
    print(er)
"""
def AbyB( a , b):
    try :
        c = ((a+b) / (a-b))
    except : #ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print( c )


AbyB( 5 , 5 )


try :
    p = 2 + 'k'
    print(p)
except TypeError :
    print("an type error !")
except :
    print("an anusal error !")
else :
   print("end")
finally :
    print("an permenaent statement")

    
try :
    pass

except ArithmeticError :
        print ("This statement is raising an arithmetic exception.")

finally :
    print( "Success!" )



try :
    f = open('magdy.txt' , 'w')
    f.write("i love checolote")
    print(f.read)
except :
    print(" an error occured ")
