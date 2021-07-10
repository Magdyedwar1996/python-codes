sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence = sentence.split(" ")
#print(sentence)
same_letter_count = 0
for i in range(len(sentence)):
    if (len(sentence[i])) == 1 or sentence[i][0]==sentence[i][-1]:
        same_letter_count += 1

#print(same_letter_count)