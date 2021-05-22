import colorgram
colours = colorgram.extract("merna.jpg", 50)
RGB_colors = []
for color in colours :
    RGB_colors.append(color.rgb)

for i in range(0, len(RGB_colors)-2, 2):
    print(str(RGB_colors[i]) + "   ///  " + str(RGB_colors[i+1]) )


print("#"*100)

colours = colorgram.extract("merna.jpg", 50)
RGB_colors = []
for color in colours :
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r, g, b )
    RGB_colors.append(new_colour)


for i in range( len(RGB_colors)):
    print(RGB_colors[i])

