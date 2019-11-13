#define longest() function
def longest():
 string = ["I", "am", "the", "baddest", "in", "town"]

 count=0
 for i in string:
    if len(i)> count:
        count =len(i)
        word = i
 print("The longest word is: " +  word)

#call longest() function
longest()
