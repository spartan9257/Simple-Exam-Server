from os import path
import os
#Provides a user menu to parse through the various scripts
print("0. Exit")
print("1. Initiate server")
print("2. Process results")
print("3. Generate certificates")
valid_input = False
while(not valid_input):
    #Get user input
    choice = int(input("Please choose an option: "))
    if choice < 0 or choice > 3:
        print("Invalid input!")
    else:
        break
#Determine user input and execute the script
if choice == 0:
    os.system("exit")
elif choice == 1:
    os.system("python server.py")
elif choice == 2:
    os.system("python process_exams.py")
elif choice == 3:
    os.system("python create_certifications.py")
else:
    os.system("exit")
