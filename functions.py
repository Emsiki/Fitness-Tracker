#This file simply has all of the custom functions that I will be using 



#Returns the data that is inputted as an array of 3 integers
def current(currentDate):
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

    return [int(month), int(day), int(year)]
