"""
026
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case
"""
word = input("enter a word plz : ")
vowels = ["a", "A", "i", "I", "e" , "E","O", "o","u","U"]
if word[0] in vowels :
    print(word +"way")
else :
    length = len(word)
    newword = word[1:length]
    print(newword + word[0]+"ay")