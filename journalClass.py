#This files contains a journal class that helps the user to manage their journal
import functions

class Journal:

    def __init__(self, text, date, time):
        self.text = text
        self.date = date
        self.time = time

    def dateAndTime(self):
        
        month = function.prompt("What month is it?: ", "", "Int") 
        day = function.prompt("What day is it?: ", "", "Int") 
        year = function.prompt("What year is it?: ", "", "Int") 

        self.date = f"{month}/{day}/{year}"

        hour = functions.prompt("What hour is it?: ", "", "Int")
        minute = functions.prompt("What minute is it?: ", "", "Int")

        self.time = f"{hour}:{minute}"
        


















