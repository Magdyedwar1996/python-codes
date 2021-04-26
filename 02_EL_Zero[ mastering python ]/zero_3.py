user = {
    'name'    : 'magdy' ,
    'age'     : ' 23 ' ,
    'country' : ' egypt'
       }
print(user)
print(type(user))
print(user.values())
print(user.keys())
print(len(user))
print(user['name'])
print(user['age'])

print("="*50)  # separator

user['friend'] = 'sameh'
print(user)
user.update({'father' : 'edwar' , 'mother' : " mariam"})
print(user)

print("="*50)  # separator

all_items = user.items()
print(all_items)

a = ('magdy' , ' sameh' , ' peter' )
b = ('name_1' , 'name_2' , 'name_3')
DICT = dict.fromkeys(b,a)
print(DICT)





























