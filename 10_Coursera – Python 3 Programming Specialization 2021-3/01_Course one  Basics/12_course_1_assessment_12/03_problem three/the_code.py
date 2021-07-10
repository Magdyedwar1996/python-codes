stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = sent.split(" ")
print(sent)
#['The', 'water', 'earth', 'and', 'air', 'are', 'vital']
acro=''
for i in range(len(sent)):
    if sent[i] in stopwords :
        continue
    else:
        acro+=sent[i][0].upper()
        acro += sent[i][1].upper()
        if(i != len(sent)-1):
            acro += ". "
print("'"+acro+"'")
#for i in range(len(org))
