from exerciseClass import Exersice, Workout, Cycle
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
    
    answer = prompt("Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics in the form of maxes\n(V)iew graphics based on past data\n(M)anually change the time\n(H)ard reset\n(R)ank:\n", "ETSVMHR", False)

    return answer

def enterWorkoutData():
    
    happendBefore = open("happendBefore.txt", "a")
    happendBefore = open("happendBefore.txt", "r")

    if happendBefore.read() == "":

        print("Since this is your first time entering data, before I'm able to save your workout data, I need to know a few things, please answer these following questions")
        
        regOrCustom = prompt("Would you like to make a custom workout routine, or choose from one of the many predefined workouts? (C or P): ", "CP", False)
        
        happendBefore = open("happendBefore.txt", "a")
        happendBefore.write("True")

        choicesToGenerateCustom()


        if regOrCustom == "R":
            #here I would give help them generate an instace of the "Workout" Class
            pass

        elif regOrCustom == "C":
            choicesToGenerateCustom()
            

        workout = open("collectedData.txt", "a")

    elif happendBefore:



        continue_ = prompt("Would you like to continue with your current workout routine? (Y or N): ", "YN", False)
        

        if continue_ == "Y":

            
            workout = open("collectedData.txt", "a")

        
        else:
            regOrCustom = prompt("Would you like to make a custom workout routine, or choose from one of the many predefined workouts? (C or P): ", "CP", False)

            if regOrCustom == "C":
            #here I would give help them generate an instace of the "Workout" Class
                pass

            elif regOrCustom == "P":
                choicesToGenerateCustom()
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


#The prompt function has 3 arguments
#The inputs argument will be used to ask the user for their input and print out the input listed
#the preferedInputs argument is if the user wants to list preferedInputs but strictly for characters
#The intr argument is for testing if the users input is a string or an integer
#for the intr argument Int or String, should be used, or False if entering a preferedInput
#Function will not work if both intr and preferedInputs arguments are filled out
#if using intr argument preferedInputs should be set to ""

def prompt(inputs, preferedInputs, intr):
    checked = False
    trigger = False
    ticker = 0
    inp = input(inputs)
    inp = inp.upper()
    prompts = []
    if preferedInputs:

       while not checked:
            for num in inp: 
                if num not in preferedInputs:
                    if ticker == 0:
                        print("Sorry, that is not a proper response")
                        prompts.append(prompt(inputs, preferedInputs, False))
                        trigger = True
                        ticker += 1

                    
            checked = True

#This intr section is strictly for number / string, inputs, while the top is for char with 1 character prefered inputs for navigations

    elif intr == "Int":
       
        while not checked:
            for num in inp: 
                if num in 'ABCDEFGHIJKLMNOPQRSTUVQXYZ-=_+/.,<>?;:':
                    if ticker == 0:
                        print("Sorry, that is not a proper response")
                    
                        prompts.append(prompt(inputs, "", "Int"))
                        trigger = True
                        ticker += 1
                    
                    
            checked = True
            
    
                
    elif intr == "String":
         
        while not checked:
            for num in inp: 
                if num in '1234567890-=_+/.,<>?;:':
                    if ticker == 0:

                        print("Sorry, that is not a proper response")
                        prompts.append(prompt(inputs, "", "String"))
                        trigger = True
                        ticker += 1
                    
   
            checked = True


    if trigger:
        return prompts[-1]
    else:
        return inp

    
    


def choicesToGenerateCustom():
    dayCount = prompt("How many days are in your workout cycle? (for ex. if you are doing push pull legs, you would have push day, pull day, leg day, and then a rest day until the cycle repeats itself): ", "", "Int")
    diffNum = prompt("Are the number of exercises in each day different? (Y or N): ", "YN", False)
    Workout = []
    Cycle = []
    if diffNum == "Y":
        for day in range(int(dayCount)):
            restDay = prompt(f"Is day #{day + 1} your rest day? (Y or N): ", "YN", False)
            if restDay == "N":
                numExer = prompt(f"How many exercises are in day #{day + 1} of your cycle?: ", "", "Int")
                for i in range(int(dayCount)):
                    dayName = prompt(f"What is the name of day #{i + 1}?: ", "", "String")      
                    for j in range(int(numExer)):
                        exerciseName = prompt(f"What is the name of workout #{j + 1} on {dayName} day: ", "", "String")
                        exerciseTime = prompt("How much time does this exersice take (In seconds)?: ", "", "Int")
                        exerciseRestAfter = prompt("How long do you rest for after this workout? (In seconds)?: ", "", "Int")
                        Workout.append(Exersice(exerciseName, exerciseTime, exerciseRestAfter))

                Cycle.append(Workout)
                Workout = []



            else:   
                Cycle.append("RestDay")

    else:    
        numExer = prompt("How many exercises are in there in each day of your cycle?", "", "Int")
        for i in range(int(dayCount)):
            dayName = prompt(f"What is the name of day #{i + 1}?: ", "", "String")      
            for j in range(int(numExer)):
                exerciseName = prompt(f"What is the name of workout #{j + 1} on {dayName} day: ", "", "String")
                exerciseTime = prompt("How much time does this exersice take (In seconds)?: ", "", "Int")
                exerciseRestAfter = prompt("How long do you rest for after this workout? (In seconds)?: ", "", "Int")
                Workout.append(Exersice(exerciseName, exerciseTime, exerciseRestAfter))

            Cycle.append(Workout)
            Workout = []
    
    return Cycle


def choicesToGenerateReg():
    pass



