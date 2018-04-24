#Series of problem(4 max) brake those problems into seperate if elif and else codes
def TechSupport():
    print("This is tech suport")
    print("Pick 1-4 to describe your problem.")
#Types in problem
    print("1: Application or app is not working correctly")
    print("2: Device malfunction")
    print("3: Virus")
    print("4: Malware")
    answer = input()
    print(answer)
#Answers to problems
    if answer == ("1"):
        print("Quit and restart application or app")
    if answer == ("2"):
        print("Shut down and restart device. Works for all types of devices.")
    if answer == ("3"):
        print("Restart your computer and run anti virus software.")
    if answer == ("4"):
        print("Download and install malware bytes. Once installed, run a full sweep of computer.")

    elif answer == (" "):
        print("You did not pick a problem.")
