
import time as t
import functions

def main():
    
    choice = functions.choice()

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