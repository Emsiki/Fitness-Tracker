# Basic Wishes:
#Create a workout class that has predefined archTypes, and have a class that inherites off of that class, 
#Which can allow you to create your own custom workouts
class Cycle:
    
    def __init__(self, name, length, workouts):
        self.name = name
        self.length = length
        self.workouts = workouts

class Workout:

    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises


class Exersice:

    def __init__(self, name, sets, time, restAfter):
        self.name = name
        self.sets = sets
        self.time = time
        self.restAfter = restAfter
        

        

        
        

