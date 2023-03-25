import exerciseClass 
import json
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

    
def enterWorkoutData():
    
    collectedData = open("collectedData.txt", "r")
    

    if collectedData.read() == "":
        collectedData.close()

        print("Since this is your first time entering data, before I'm able to save your workout data, I need to know a few things, please answer these following questions")
        
        regOrCustom = prompt("Would you like to make a custom workout routine, or choose from one of the many predefined workouts? (C or P): ", "CP", False)
        
      

        if regOrCustom == "R":
            
            pass

        elif regOrCustom == "C":
            
            
            collectedData = open("collectedData.txt", "a")
            collectedData.close()
            #makes a custom workout, converts it to JSON and saves it
            workout.write(f"{json.dumps(choicesToGenerateCustom())}")

            collectedData = open("collectedData.txt", "r")
            collectedData.close()
            print(type(json.loads(workout.read())))


      

    else:



        continue_ = prompt("Would you like to continue with your current workout routine? (Y or N): ", "YN", False)
        

        if continue_ == "Y":

            
            workout = open("collectedData.txt", "r")
            cycle = json.loads(workout.read())

        
        else:
            regOrCustom = prompt("Would you like to make a custom workout routine, or choose from one of the many predefined workouts? (C or P): ", "CP", False)

            if regOrCustom == "C":
                workout = open("collectedData.txt", "w")
                workout.write(f"{json.dumps(choicesToGenerateCustom())}")
                

            elif regOrCustom == "P":
                
                pass


def talkToAssistant():
    pass


def submitGeneralStats():
    pass


def viewGraphics():
    pass


def hardReset():
    workOutReset = open("collectedData.txt", "w")
    workOutReset.close()
    


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
    inpCopy = inp.upper()
    prompts = []
    if preferedInputs:

       while not checked:
            for num in inpCopy: 
                if num not in preferedInputs or len(num) == 0:
                    if ticker == 0:
                        print("Sorry, that is not a proper response")
                        prompts.append(prompt(inputs, preferedInputs, False))
                        trigger = True
                        ticker += 1

                    
            checked = True

#This intr section is strictly for number / string, inputs, while the top is for char with 1 character prefered inputs for navigations

    elif intr == "Int":
       
        while not checked:
            for num in inpCopy: 
                if num in 'ABCDEFGHIJKLMNOPQRSTUVQXYZ-=_+/.,<>?;: ' or len(num) == 0:
                    if ticker == 0:
                        print("Sorry, that is not a proper response")
                    
                        prompts.append(prompt(inputs, "", "Int"))
                        trigger = True
                        ticker += 1
                    
                    
            checked = True
            
    
                
    elif intr == "String":
         
        while not checked:
            for num in inpCopy: 
                if num in '1234567890-=_+/.,<>?;:' or len(num) == 0:
                    if ticker == 0:

                        print("Sorry, that is not a proper response")
                        prompts.append(prompt(inputs, "", "String"))
                        trigger = True
                        ticker += 1
                    
   
            checked = True


    if trigger:
        return prompts[-1]
    else: 
        return inpCopy
 
    

#The choicesToGenerateCustom function returns a custom workout in the form of a 2d array
def choicesToGenerateCustom():
    dayCount = prompt("How many days are in your workout cycle, including rest days? (for ex. if you are doing push pull legs, you would have push day, pull day, leg day, and then a rest day until the cycle repeats itself): ", "", "Int")
    diffNum = prompt("Are the number of exercises in each day different? (Y or N): ", "YN", False)
    Exersice1 = []
    
    Cycle = []
    if diffNum == "Y":
        for day in range(int(dayCount)):
            restDay = prompt(f"Is day #{day + 1} a rest day? (Y or N): ", "YN", False)
            if restDay == "N":
                dayName = prompt(f"What is the name of day #{day + 1}?: ", "", "String")  
                numExer = prompt(f"How many exercises are in {dayName} day : ", "", "Int")
                    
                for j in range(int(numExer)):
                    exerciseName = prompt(f"What is the name of workout #{j + 1} on {dayName} day: ", "", "String")
                    exerciseSets = prompt(f"How many sets do you do of {exerciseName}?: ", "", "Int")
                    exerciseTime = prompt("How much time does each set of this exersice take not including rest time (In seconds) ?: ", "", "Int")
                    exerciseRestAfter = prompt("How long do you rest for after each set of this workout? (In seconds)?: ", "", "Int")
                    
                    Exersice1.append([exerciseName, exerciseSets, exerciseTime, exerciseRestAfter])
                        
                Cycle.append(Exersice1)
                Exersice1 = []

            else:   
                Cycle.append("RestDay")
                          

    else:    
        numExer = prompt("How many exercises are in there in each day of your cycle?: ", "", "Int")
        for i in range(int(dayCount)):
            restDay = prompt(f"Is day #{i + 1} a rest day? (Y or N): ", "YN", False)
            if restDay == "N":
                dayName = prompt(f"What is the name of day #{i + 1}?: ", "", "String")      
                for j in range(int(numExer)):
                    exerciseName = prompt(f"What is the name of workout #{j + 1} on {dayName} day: ", "", "String")
                    exerciseSets = prompt(f"How many sets do you do of {exerciseName}?: ", "", "Int")
                    exerciseTime = prompt("How much time does each set of this exersice take not including rest time (In seconds)?: ", "", "Int")
                    exerciseRestAfter = prompt("How long do you rest for after each set of this workout? (In seconds)?: ", "", "Int")
                    
                    Exersice1.append([exerciseName, exerciseSets, exerciseTime, exerciseRestAfter])
                    
                Cycle.append(Exersice1)
                Exersice1 = []
                
            else:
                Cycle.append("RestDay")
            

    return Cycle


def choicesToGenerateReg():
    pass



def journal():
    pass







