stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.split(" ")
#['The', 'organization', 'for', 'health,', 'safety,', 'and', 'education']
acro=""
for i in range(len(org)):
    if org[i] in stopwords :
        continue
    else:
        acro+=org[i][0].upper()

print(acro)
#for i in range(len(org))

