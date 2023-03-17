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
    currentTime = input("What is the current time in the format H:MM?: ")
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

    print("Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics in the form of maxes\n(V)iew graphics based on past data\n(M)anually change the time\n(H)ard reset")
    answer = input().upper()

    while answer not in "ETSVMH":
        print("That is not a valid choice, Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics\n(V)iew graphics based on past data\n(M)anually change the time\n(H)ard reset")
        answer = input().upper()

    return answer



def enterWorkoutData():
    
    happendBefore = open("happendBefore.txt", "a")
    happendBefore = open("happendBefore.txt", "r")

    if happendBefore.read() == "":

        print("Since this is your first time entering data, before I'm able to save your workout data, I need to know a few things, please answer these following questions")
        
        regOrCustom = input("Since this is your time enterting data, Would you like to make a custom workout routine, or choose from one of the many predefined workouts? (Y or N): ")
        
        happendBefore = open("happendBefore.txt", "a")
        happendBefore.write("True")

        while regOrCustom.upper() not in "YN":
            regOrCustom = input("That is not a correct response, please enter 'Y' or 'N': ")


        if regOrCustom.upper() == "N":
            #here I would give help them genorate an instace of the "Workout" Class
            pass

        elif regOrCustom.upper() == "Y":
            #here I would give help them genorate an instance of the "CustomWorkout" Class
            pass
        workout = open("collectedData.txt", "a")

    elif happendBefore:

        continue_ = input("Would you like to continue with your current workout routine? (Y or N): ")

        while continue_.upper() not in "YN":
            continue_ = input("That is not a propper response, please enter a response in the format (Y or N)")

        if continue_.upper() == "Y":

            workout = open("collectedData.txt", "a")
        
        else:
            pass


def talkToAssistant():
    pass


def submitGeneralStats():
    pass


def viewGraphics():
    pass


def hardReset():
    workOutReset = open("collectedData.txt", "w")
    happendBeforeReset = open("happendBefore.txt", "w")
    workOutReset.write('')
    happendBeforeReset.write('')
    workOutReset.close()
    happendBeforeReset.close()


def rank():
    pass



    
# Below are functions that are going to be used in this file and not any others:

def repromt():
    pass



def choicesToGenerateCustom():
    numExer = input("How many exercies are in your workout?: ")
    checked = False

    while not checked:
        for num in numExer:
            if num not in "1234567890":
                numExer = input("That is not a valid response, How many exercies are actually in your workout?: ")
            
            else:
                checked = True
        
            
    for i in range(int(numExer)):
        workoutName = input(f"What is the name of the workout #{i + 1}?: ")
        workoutTime = input("How much time does this exersice take (In seconds)?: ")
        workoutRestAfter = input("How long do you rest for after this workout?")
        


def choicesToGenerateReg():
    pass



