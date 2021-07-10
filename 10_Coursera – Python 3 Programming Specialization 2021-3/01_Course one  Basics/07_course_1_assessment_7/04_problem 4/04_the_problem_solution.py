sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence = sentence.split(" ")
num_a_or_e = 0
A_yes = " "
E_yes = " "
for i in range(len(sentence)):
    for j in range(len(sentence[i])):
        if(sentence[i][j] == 'a') or (sentence[i][j]== 'e'):
            A_yes = 'a'
            E_yes = 'e'
    if A_yes =='a' or E_yes =='e':
        num_a_or_e += 1
        A_yes = ' '
        E_yes = ' '

#print(num_a_or_e)