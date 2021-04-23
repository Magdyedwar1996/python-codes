 #   dictionary


 # dictionary one
user = {
     "name"    :     "magdy" ,
     "age"     :     23     ,
     "country" :     'egypt' ,
    "skills"   :     { ' html ' , ' css ' , ' python '} ,
    "name "    :    " kero "
 }
print(user)
print(user["name"])
print(user["skills"])
print(user.get("country"))   # get( )

print(user.keys())  # keys
print(user.values())  # values


             # dictionary two
languages =   {
    "one" :
        {
            "name" : "css" ,
            "progress" :"80 %"
        } ,

    "two" :
        {
            "name"      : "python",
            "progress"  : "90 %"
        } ,
    "three" :
        { "name" : 'c language' ,
           "progress" :
               {
                   "first" : "80%",
                   "second" : '100%'
               }
        }
             }

print(languages)
print(languages['one']['name'])
print(languages['two']['progress'])
print(languages['three']['progress']['first'])
print(languages['three']['progress']['second'])
print(len(languages))
print(len(languages['two']))




family = {
                "son_one_edwar" : {

                             'son_1'  : {

                                          "name" : 'magdy' ,
                                          "age"  : 23 ,
                                          "country" : 'Egypt'
                                         } ,

                             'son_2'  :{
                                          "name" : 'neven' ,
                                          "age"  : 21,
                                          "country" : 'Egypt'
                                          }    ,
                             'son_3'  : {
                                          "name" : 'mark' ,
                                          "age"  : 15 ,
                                          "country" : 'Egypt'
                                       }
                           } ,

                "son_two_kamal " : {
                        'son_1':    {
                                    "name"     : 'wassem',
                                    "age"      : 16 ,
                                    "country"  : 'lebia'
                                    },

                        'son_2'  :  {
                                "name"       : 'wafik',
                                 "age"       : 14  ,
                                 "country"   : 'Egypt'

                                  },

                        'son_3' :  {
                                 "name"  : 'emmy',
                                 "age"  : 7,
                                 "country": 'Egypt'
                                   }
                                     ,

                        " son_4" : {
                                 "name"  : 'wael',
                                 "age"    :  4 ,
                                 "country": 'Egypt'
                                   }} ,

                "son_three_nessem" :  {
                        'son_1':    {
                                    "name"     : 'michael',
                                    "age"      : 7 ,
                                    "country"  : 'egypt'
                                    }  ,

                        'son_2'  :  {
                                "name"       : 'mera',
                                 "age"       : 4  ,
                                 "country"   : 'Egypt'

                                  },
                        'son_3' :  {
                                 "name"  : 'melessia',
                                 "age"  : 1,
                                 "country": 'Egypt'
                                   }
                                    }
         }


print(family)
