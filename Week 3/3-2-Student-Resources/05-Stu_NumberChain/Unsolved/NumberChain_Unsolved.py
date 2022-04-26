# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_input = input('How many number?')
    
        # Loop through the numbers. (Be sure to cast the string into an integer.)
    for each_n in range(user_input):
        print(each_n)

        # Print each number in the range
       

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")