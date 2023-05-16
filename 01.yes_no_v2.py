
show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user if they have played before
    show_instructions = input("Have you played"" this slay queen of a game before? ").lower()
    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("That's great!")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "yes"
        print("Show instructions")

    # If they say no, output 'display instructions'
    else:
        print("Answer yes or no please")
