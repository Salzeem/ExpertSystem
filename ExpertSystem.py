import pandas as p 



#Expert System function, The basic functionality 
def expertsystem_handle_queries():
    print("Movie Expert System called ")
    movie_data_dataFrame = p.read_excel('MovieData.xlsx', sheet_name='movies')
    changed_df = movie_data_dataFrame
    #movie_data_dataFrame.info()

        #Take the most common genre 
        #Ask the user if it is within this genre, if yes, delete everything not peterning to this genre 
        #Ask the user if the year is before or after a certain limit, if yes delete everything before that year
        #Ask the user if the movie is above  a certain hour, if yes remove everything below that hour 
        #Ask the user 

        #At any point the user asks why then bring out a decision tree or the logic/data frame of what you have done 
        #At each step we keep transforming the dataframe until we reach a certain movie, if multiple movies keep reappearing then we display the one with 
        #The highest rating 



    while(True):

        # Ill go with the most common questions 
        most_common_genre = changed_df['Genre'].str.split(', ').explode().value_counts().idxmax() #This takes too long lmao
        year_midpoint = movie_data_dataFrame['Year'].median()
        runtime_midpoint = movie_data_dataFrame['Runtime (Minutes)'].median() 

        print ("This is the most common genre " + most_common_genre)

        genre_question = input("Is it a or an " + most_common_genre + " movie? : ")

        if (genre_question == 'yes'):
            #modify the pandas df to only include genres that have drama in them 
            print("Modify the pandas df to only include the genres that do have drama in them ")
            changed_df = movie_data_dataFrame[  movie_data_dataFrame["Genre"] == most_common_genre] 
            print ( changed_df.head()) 
        else:
            #modify the pandas df to only include genres that do not have drama in them 
            print("Modify the pandas df to only include genres that do not have drama in them ")
            changed_df = movie_data_dataFrame[  movie_data_dataFrame["Genre"] != most_common_genre] 
            print ( changed_df.head()) 


        year_question = input("Was the movie before the year " + str(year_midpoint) + "(inclusive) : ")

        if (year_question == 'yes'):
            print("Modify the pandas df to only allow movie before the year ")
            changed_df = changed_df[changed_df['Year'] <  int(year_midpoint)]
        else:
            print("Modify the pandas df to only include the years after that time period ")
            changed_df = changed_df[changed_df['Year'] > int(year_midpoint)]

        
        runtime_question = input("Is the movie longer than " + str( runtime_midpoint) +  "? : ")

        if (runtime_question == 'yes'):
            print("Modify the pandas df to only allow runtime longer than the midpoint specified ")
            changed_df = changed_df[changed_df['Runtime (Minutes)'] <  int(runtime_midpoint)]

        else:
            print("Modify the pandas df to only allow the runtime before the specified midpoint ")
            changed_df = changed_df[changed_df['Runtime (Minutes)'] >  int(runtime_midpoint)]

        if (changed_df.size > 1 ): 
            print("Thank you for answering these questions, I have about " +  str (changed_df.size) + " In mind, would you like to to try and narrow my search down? ") 
            narrow = input() 
            if (narrow == 'no'):
                break 
            else:
                while(changed_df.size> 10):
                    mcommon = changed_df['Genre'].str.split(', ').explode().value_counts().idxmax() #This takes too long lmao
                    genre_question = input("Is it a or an " + mcommon + " movie? : ")
                    if (genre_question == 'yes'):
                        changed_df = movie_data_dataFrame[  movie_data_dataFrame["Genre"] == mcommon] 
                        
                    else:
                        changed_df = movie_data_dataFrame[ movie_data_dataFrame["Genre"] != mcommon]



    print(changed_df.head())
    
    




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
            expertsystem_handle_queries()
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



