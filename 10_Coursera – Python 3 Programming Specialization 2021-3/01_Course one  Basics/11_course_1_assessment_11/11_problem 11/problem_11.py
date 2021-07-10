wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds =wrds
for i in range(len(wrds)):
    past_wrds[i] = wrds[i]+ "ed"

print(past_wrds)