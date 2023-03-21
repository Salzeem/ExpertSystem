import pandas as p 



#Expert System function, The basic functionality 
def expertsystem_handle_queries():
    print("Movie Expert System called ")
    movie_data_dataFrame = p.read_excel('MovieData.xlsx', sheet_name='movies')

    while (True ): 
        #Take the most common genre 
        #Ask the user if it is within this genre, if yes, delete everything not peterning to this genre 
        #Ask the user if the year is before or after a certain limit, if yes delete everything before that year
        #Ask the user if the movie is above  a certain hour, if yes remove everything below that hour 
        #Ask the user 

        #At any point the user asks why then bring out a decision tree or the logic/data frame of what you have done 
        #At each step we keep transforming the dataframe until we reach a certain movie, if multiple movies keep reappearing then we display the one with 
        #The highest rating 

        most_common_genre = movie_data_dataFrame['Genre'].str.split(', ').explode().value_counts() 




def add_custom_movie():
    #Ask the user what the name of the movie is 
    #Ask the user about the genre of the movie 
    #Ask the user about how long the movie is 
    #Ask the user if they know the director and ask if they can provide a brief description of the movie, they can refuse to do so, that is fine 
    #Get all the data from the excel file and add it to the dataframe, then append the new information into the same dataframe and overwrite the excel file 

    print("Adding custom movie called ")

    return 

def delete_movie():

    #Ask the user if this is a movie they created or if it is a movie the system already knows 
    #if it is a movie they created then we look for it in the excel file and ask them which movie it is they want to delete 
    #Otherwise we narrow the search down by simply asking them what the name of the movie is, turn evertyhing into lower cased and use pandas to get the row/col 
    #Delete the row/col combo and call it a day 
    print("Delete Movie called ")
    return 


def main():
    print("Welcome to the Movie Expert System")
    while True:
        user_input = input("Press E to use the Movie Expert System, press A to Add a movie to my knowledge, press D to delete a movie, press Q to exit: ")
        if user_input.upper() == 'E':
            print("Using the Movie Expert System...")
        elif user_input.upper() == 'A':
            print("Adding a movie to my knowledge...")
        elif user_input.upper() == 'D':
            print("Deleting a movie...")
        elif user_input.upper() == 'Q':
            print("Thank you for using our service! ")
            print("Exiting the program...")
            return 
        else:
            print("Invalid input. Please try again.")

main()



