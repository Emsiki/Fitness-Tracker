
import time
import functions

def main():
    openedBefore = open("collectedData.txt", "r")
    
    if not openedBefore.read():
        helpOrNot = functions.prompt("Welcome to   F i t n e s s T r a c k e r   your console based fitness tracker that you've always dreamed of, since this is your first time using this program, would you like instructions?", "YN", "")
    
    if helpOrNot == "Y":
        print("This Fitness Tracker comes with tons of useful features, being able to view graphs for specific exercies that you've inputted the statistics for, talking to a virtual assistant (Powered by Chat-GPT), journaling about your day / workout, and viewing where you fall in comparison to others of your same sex, bodyweight, and age! If you would like help in more detail, simply type 'H' in the main menu!")



    choice = functions.prompt("Please choose one of the following actions:\n(E)nter data\n(T)alk to a virtual assistant\n(S)ubmit bodyweight, sex, and age\n(V)iew graphics based on past data\n(M)anually change the time\nH(A)rd reset\n(R)ank\n(J)ournal\n(H)elp:\n", "AETSVMHR", False)

    if choice == "V":
        functions.viewGraphics()
    elif choice == "E":
        functions.enterWorkoutData()
    elif choice == "M":
        functions.manualDate()
        functions.manualTime()
    elif choice == "T":
        functions.talkToAssistant()
    elif choice == "S":
        functions.submitGeneralStats()
    elif choice == "A":
        functions.hardReset()
    elif choice == "R":
        functions.rank()
    elif choice == "J":
        functions.journal()
    elif choice == "H":
        #This just explains all of the features, I still need to implement some of them though
        whatWouldYouLikeHelpWith = functions.prompt("What specific feature would you like help with? (E)nter data\n(T)alk to a virtual assistant\n(S)ubmit bodyweight, sex, and age\n(V)iew graphics based on past data\n(M)anually change the time\nH(A)rd reset\n(R)ank\n(J)ournal:\n")
        if whatWouldYouLikeHelpWith == "E":
            pass
        elif whatWouldYouLikeHelpWith == "T":
            pass
        elif whatWouldYouLikeHelpWith == "S":
            pass
        elif whatWouldYouLikeHelpWith == "V":
            pass
        elif whatWouldYouLikeHelpWith == "M":
            pass
        elif whatWouldYouLikeHelpWith == "A":
            pass
        elif whatWouldYouLikeHelpWith == "R":
            pass
        elif whatWouldYouLikeHelpWith == "J":
            pass
if __name__=="__main__":
    main()












         #print( '    __      __         .__                                         '  + 
# '   /  \    /  \  ____  |  |    ____   ____    _____    ____        '  + 
# '   \   \/\/   /_/ __ \ |  |  _/ ___\ /  _ \  /     \ _/ __ \       '  + 
# '    \        / \  ___/ |  |__\  \___(  <_> )|  Y Y  \\  ___/       '  + 
# '     \__/\  /   \___  >|____/ \___  >\____/ |__|_|  / \___  >      '  + 
# '          \/        \/            \/              \/      \/       '  + 
# '                                                                   '  + 
# '     __                                                            '  + 
# '   _/  |_  ____                                                    '  + 
# '   \   __\/  _ \                                                   '  + 
# '    |  | (  <_> )                                                  '  + 
# '    |__|  \____/                                                   '  + 
# '                                                                   '  + 
# '                                                                   '  + 
# '   ___________.__   __                                             '  + 
# '   \_   _____/|__|_/  |_  ____    ____    ______  ______           '  + 
# '    |    __)  |  |\   __\/    \ _/ __ \  /  ___/ /  ___/           '  + 
# '    |     \   |  | |  | |   |  \\  ___/  \___ \  \___ \            '  + 
# '    \___  /   |__| |__| |___|  / \___  >/____  >/____  >           '  + 
# '        \/                   \/      \/      \/      \/            '  + 
# '                                                                  ' )    