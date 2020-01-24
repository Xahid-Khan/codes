command = ""
while command != "quit":
    command = input(": ").lower()
    if command == "start":
        print("start the car ... ready to go")
    elif command == "stop":
        print("stop the car")
    elif command == "help":
        print(
              "start _ to start the car"
              "stop _ to stop the car"
              "quit _ to exit"
              )
    else:
        print("I don't understand")



