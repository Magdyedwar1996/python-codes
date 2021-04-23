a = [1, 2, 3]
try:
   # print("fifth element = %d" % (a[4]))
    print("Second element = %d"%(a[1]))
    print("first element = %d" % (a[0]))
    print("Fourth element = %d" % (a[3]))

except IndexError:
    print("magdy loves HER ")
    try:
        #print("fifth element = %d" % (a[4]))
        print("Second element = %d" % (a[1]))
        print("first element = %d" % (a[0]))
        print("Fourth element = %d "%(a[3]))

    except IndexError:
        print("An error occurred")
print("magdy loves her ")
