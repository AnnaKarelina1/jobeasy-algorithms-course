

#1 Longest string

phrase=input("Phrase:")
phrase=phrase.split(" ")
print(phrase)
longest_word=""

for i in phrase:
    if len(i)>len(longest_word):
        longest_word=i
print(longest_word)

# Enter an irregular string (that means it may have space at the beginning of a string,
# at the end of the string, and words may be separated by several spaces). Make the string regular
# (delete all spaces at the beginning and end of the string, leave one space separating words).

phrase=input("Phrase:")
phrase=phrase.split(" ")
new_phrase=[]

for i in phrase:
    if i.isalpha():
        new_phrase.append(i)
print(" ".join(new_phrase))



# Write a Python function, which will count how many times
# a character (substring) is included in a string. DON’T USE METHOD COUNT

# #

def char_result(phrase):
    counting={}
    for char in phrase:
        if char.isalpha():
            if char in counting:
                counting[char]+=1
            else:
                counting[char]=1
    return counting

phrase=(input("Write a string: "))
print(char_result(phrase))




# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE

def replace_substring(phrase,n,k):
    phrase=phrase.split()
    if n in phrase:
        index=phrase.index(n)
        phrase[index]=k
    return " ".join(phrase)


phrase=(input("Write a string: "))
n=(input("Actual substring: "))
k=(input("New substring: "))
print(replace_substring(phrase,n,k))

