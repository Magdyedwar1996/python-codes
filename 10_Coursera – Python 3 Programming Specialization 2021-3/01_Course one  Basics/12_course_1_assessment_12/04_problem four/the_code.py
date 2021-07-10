p_phrase = "was it a car or a cat I saw"
new_p_phrase = ""
for i in range(len(p_phrase)):
        new_p_phrase += p_phrase[i]

r_phrase = ""
r_phrase = new_p_phrase[::-1]
print(r_phrase)

print(new_p_phrase)