def create_cast_list(filename):

    cast_list = []
    # use with to open the file filename
    with open(filename) as File:
        # use the for loop syntax to process each line
        for line in File:
            temp_list = line.split(",", maxsplit=1)
            cast_list.append(temp_list[0])
            # and add the actor name to cast_list

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
