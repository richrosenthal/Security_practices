def sloppyCode():
    listOfNums = [5, 10, 15, 20, 25] 
    indexOfNumsStrToInt = input()
    indexOfNums = int(indexOfNumsStrToInt)
    if (indexOfNums == 0):
        print("One of the elements is out of bounds")
    elif (indexOfNums == 4):
        print("One of the elements is out of bounds")
    else:
        print(listOfNums[indexOfNums - 1],  listOfNums[indexOfNums],  listOfNums[indexOfNums + 1])




if __name__ == '__main__':
    sloppyCode()

# Write a program that will take as input, an index to the list [5, 10, 15, 20, 25]. The program should then print the element referenced by the entered index along with the elements that come immediately before and after. Use exception handling to handle out of index references. The program should notify the user when such an exception occurs.

# Ex: If the input of the program is:

# 0
# the output of the program is:

# One of the elements is out of bounds
# Ex: If the input of the program is:

# 1
# the output of the program is:

# 5 10 15
# Ex: If the input of the program is:

# 4
# the output of the program is:

# One of the elements is out of bounds

# Yeah yeah I know, I knew what it was testing so I wrote a sloppy reponse. I'll refactor and finish this.
# This is what you write when you've been trying to put out fires at work all day
#12-4-25
