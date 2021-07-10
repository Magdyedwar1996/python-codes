inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
item = []
for i in range(len(inventory)):
        item = inventory[i].split(",")
        print("The store has{0} {1}, each for{2} USD.".format(item[1],item[0],item[2]))