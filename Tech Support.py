def TechSupport():
    print("This is tech suport")
    print("Type your problem.")
#Types in problem
    print("What is your problem?")
    answer = input()
    print(answer)
#Recomendations start
    if answer == ("  "):
        print("Ok. Have you tried quitting the application and then restarting it? Did that work?")
        answer = input()
        print(answer)
    else:
        print("Have you tried force quiting the aplication? Did that work?")
        answer = input()
        print(answer)

    if answer == ("Yes"):
        print("My work here is done!")
    else:
        print("Have you tried turning your computer, tablet, or phone completely off? Did that work?")
        answer = input()
        print(answer)
    if answer == ("Yes"):
        print("I was glad I could be of help!")
    else:
        print("Have you tried to restart your computer? Did that work?")
        answer = input()
        print(answer)
    if answer == ("Yes"):
        print("Glad to help!")
    else:
        print("I'm very sorry, but I reccomend now that you visit customer suport from the company you baught the product from.")
