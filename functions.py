#This file simply has all of the custom functions that I will be using 



#Returns the data as a set of 3 integers
def manualDate():
    currentDate = input("What is the currnet date in MM/DD/YYYY format?: ")
    month = ""
    day = ""
    year = ""
    storage = ""
    count = 0
    for x in currentDate:
        if x != "-" and x != "/":
            storage = storage + x
            if count == 0:
                month = storage
            elif count == 1:
                day = storage
            else:
                year = storage
        else:
            count += 1
            storage = ""

    return int(month), int(day), int(year)

#Returns the data as a set of 3 integers
def manualTime():
    currentTime = input("Please enter time in the format H:MM")
    hour = ""
    minute = ""
    storage = ""
    count = 0
    for x in currentTime:
        if x != "-" and x != ":" and x != "/" and x != ";":
            storage = storage + x
            if count == 0:
                hour = storage
            else:
                minute = storage
            
        else:
            count += 1
            storage = ""

    return int(hour), int(minute)


#Returns the players menu navigation choice in the form of a capital character 
#Possible outputs include E, T, V, S, M
#More can be added simply, just edit the while loops conditional to include more inputs and the first print statement to include more inputs
def choice():

    print("Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics\n(V)iew graphics based on past data\n(M)anually change the time")
    answer = input().upper()

    while answer not in "ETSVM":
        print("That is not a valid choice, Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics\n(V)iew graphics based on past data")
        answer = input().upper()

    return answer



def enterWorkoutData():
    
    print("First, before I'm able to save your workout data, I need to know a few things, please answer these following questions")

    


    workout = open("collectedData.txt", "a")
    workout.write("nerd")



    pass


def talkToAssistant():
    pass


def submitGeneralStats():
    pass


def viewGraphics():
    pass



