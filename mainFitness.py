
import time
import functions

def main():
    openedBefore = open("collectedData.txt", "r")

    if not openedBefore.read():
        helpOrNot = functions.prompt("Welcome to   F i t n e s s T r a c k e r   your console based fitness tracker that you've always dreamed of, since this is your first time using this program, would you like instructions?", "YN", "")
        #if helpOrNot == "Y":


    choice = functions.prompt("Please choose one of the following actions:\n(E)nter your data for today\n(T)alk to a virtual assistant\n(S)ubmit your general statistics in the form of maxes\n(V)iew graphics based on past data\n(M)anually change the time\n(H)ard reset\n(R)ank:\n", "ETSVMHR", False)

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
    elif choice == "H":
        functions.hardReset()
    elif choice == "R":
        functions.rank()

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