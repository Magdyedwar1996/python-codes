f = open('some_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()
"""
Decision = input("Do you want to continue : (y or n )")
if Decision == "y".lower():
    with open("camelot.txt") as song:
        print(song.read(2 ))# this reads only first two characters 
        print(song.read(8)) # this reads the second 8 characters 
        print(song.read()) # this will read all the remaining characters
else : 
      print("all your files are closed ")
      
"""
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line)
        print(line)

print(camelot_lines)      