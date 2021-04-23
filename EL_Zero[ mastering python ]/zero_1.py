            # set {.........}
s = { 5,7 , 8 , 9 , 8 , 4 , 7 , 8 , 9 }
print(s)
print(s)
print(s)

             # clear()
s.clear()
print(s)

              # add()
s.add(8)
print(s)


               # copy()
y = s.copy()
print(y)
y.add(7)
print(y)

               # type()
print(type(y))
u = { 7 , 9 , 6}
print(u | y | s )

               # union()
o = y.union(s)
print(u.union(y))
print(o)

                # intersection()
print(s.intersection(y))
print("-"*60)
                # intersetion_update()
qw = { 5 , 8 , 9 , 87, 56, 458 , 'magdy'}
wq = { 5 , 8, 458 ,87 ,'magdy'}
print(qw)
print(wq)
qw.difference(wq)
yt = qw.difference(wq)
print(yt)
print(qw)
qw.difference_update(wq)
cv = qw.difference_update(wq)
print(cv)
print(qw)
print("-"*60)

                # remove()
t = u.remove(9)
print(t)

                 # pop()
r = {  3 , 8  , 7 , 5 , 78 , "true" , ' none '}
e = r.pop()
print(e)

                   # update()

r.update(o)
print(r)
                    # difference()
re = {3 ,4 ,55,34,53,23,54,12,34,32,6,3,34} # { 3 , 55 ,  53  ,  12 , 32 , }
er = {4 , 98 , 34 , 23 , 'atom' , 'peter ' , 6 , 54 , 34 }
uy = re.difference(er)
print(uy)

print('='*50)            # separator
yu = re - er
print(yu)

                  # difference_update()
print("="*50)
print(re)
re.difference_update(er)
print(re)

           # symetric difference  po ^ op
po = {'peter' , 'magdy ' , 5  ,9 ,8 ,6,88, 99, 894}
op = {'sameh' , 8  , 9,87 ,88 ,5}
print(po)
print(po.symmetric_difference(op))
print(po)


print("."*50)



        # symetric_difference_update()
ds = {'peter' , 'magdy ' , 5  ,9 ,8 ,6,88, 99, 894}
sd = {'sameh' , 8  , 9,87 ,88 ,5}
print(ds)
print(ds.symmetric_difference_update(sd))
print(ds)
print(sd)


                           #issuperset()
d = { 1 , 2 ,3 , 4 , 5, 6}
e = {1 , 2,3 ,4}
print(d.issuperset(e) ) # true

                        # issupset()
de =  { 1 , 2 ,3 , 4 , 5, 6 , 7 , 8 }
ed =  {1 , 2 , 3 , 4}
print(de.issubset(ed)) # false
print(ed.issubset(de))  # true

print('*'*50)
            # isdisjoint()
ty = {10 , 14 ,54 ,87 ,89 ,65 ,78 }
yt = {12 , 54 ,74 , 69 , 321 , 415 , 1458  }
yty = {1 , 2 ,  4}
print(ty.isdisjoint(yt))
print(ty.isdisjoint(yty))


