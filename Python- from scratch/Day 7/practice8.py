#Write a function that takes a string and returns the count of vowels and consonants separately.

def count(string):
    lowerstr = string.lower()
    vowels = 0
    consonents = 0
    for i in lowerstr:
        if i =="a" or i=="e" or i=="o" or i=="i" or i=="u":
            vowels += 1
        else:
            consonents += 1
    print(f"The total number if vowels in {string} are : {vowels}")
    print(f"The total number if consonents in {string} are : {consonents}") 
     
    return(vowels, consonents)

name = input("Enter any name : ")
counting = count(name)

""" This code isn't completely correct becoz it calculate empty string as a consonent """
