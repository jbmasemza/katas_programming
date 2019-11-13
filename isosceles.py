#define isosceles() function
def isosceles():
 num = int(input("Number of rows: "))    
 for i in range (0,num+1):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print("#",end="")
    for j in range(2,i+1):
        print("#",end="")
    print()

#call isosceles() function
isosceles()
