# import re

# race_started = False

# def start_race():
#     global race_started
#     if not race_started:
#         print('The race has started!')
#         race_started = True
#     else:
#         print('The race has already begun....')

# def stop_race():
#     global race_started
#     if race_started:
#         print('FINISH LINE!')
#         race_started = False
#     else:
#         print('The race has not started yet.')

# def help_command():
#     print('Available commands:')
#     print('START - Start the race.')
#     print('STOP - Stop the race.')
#     print('QUIT - Quit the game.')

# while True:
#     user_input = input('Enter a command: ').strip().lower()

#     if re.search(r'\bstart\b', user_input):
#         start_race()
#     elif re.search(r'\bstop\b', user_input):
#         stop_race()
#     elif re.search(r'\bquit\b', user_input):
#         print('YOU QUIT THE GAME')
#         break
#     else:
#         help_command()

# import re
# while True:
#     command1 = input().lower()
#     Race = "START"
#     if re.search(command1, Race):
#         print('The race has started!')
#     else:
#         print('wrong command, type HELP to get command lines')

#     command2 = input().lower()
#     Hold = "STOP"
#     if re.search(command2, Hold):
#         print('FINISH LINE!')
#     elif re.search(command2, Race):
#         print('The race has already begun....')
#     else:
#         print('wrong command, type HELP to get command lines')
    
#     command3 = input().lower()
    # Helpp = "HELP"
    # if re.search(command3,Helpp):
    #     print('start: to start the car'
    #             'stop: to stop the car'
    #             'quit: to leave the game')

    # command4 = input().lower()
    # Final = "Quit"
    # if re.search(command4, Final):
    #     print('YOU QUIT THE GAME')
    #     break  


command = ""
race_started = False
while True:
    command = input(">>>").lower()
    if(command == 'Help'):
        print("""
start -to start the race
stop -to stop the car
quit -to end race
""")
    elif(command == "start"):
        if race_started:
            print("race already begun")
        else:
            race_started = True
            print("race has begun!")
    elif(command == "stop"):
        if not race_started:
            print("car already stopped.")
        else:
            race_started = False
            print("car has stopped.")
    elif(command == "quit"):
        print("race ended")
        break
    else:
        print
