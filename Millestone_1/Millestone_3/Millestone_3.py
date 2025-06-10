while True:
    # Start
    print("Welcome to the ultimate geography quiz, its porpuse is to test your knowledge about countries city capitals around the world")
    user_name = input("Username:").strip()
    print("""{} this quiz is composed of 3 questions each one is a 33% of your quiz so be sure to answer correctly.
    You only have 2 attempts to answer each question. Good Luck {}.""".format(user_name, user_name))

    ready = input("Are you ready?").lower().strip()    

    #score
    score = 0    

    if ready == "yes":
        # Question 1
        print("1. Which is the capital of Colombia?")
        print("""a. Bogota\nb. Santiago\nc. Madrid""")
        answer_1 = input("Answer:").lower().strip()
        attempts = 1
        while answer_1 not in ['a', 'bogota'] and attempts < 2:
            print("Wrong. Try again.")
            answer_1 = input("Answer:").lower().strip()
            attempts += 1
        if answer_1 == "a" or answer_1 == "bogota":
            print("Correct!")
            score += 33.33
            print("You got 33.33 points")
        else:
            print("The correct answer is Bogota.")

        # Question 2
        print("2. Which is the capital of Germany?")
        print("""a. Brasília\nb. Seoul\nc. Berlin""")
        answer_2 = input("Answer:").lower().strip()
        attempts = 1
        while answer_2 not in ['c', 'berlin'] and attempts < 2:
            print("Wrong. Try again.")
            answer_2 = input("Answer:").lower().strip()
            attempts += 1
        if answer_2 == "c" or answer_2 == "berlin":
            print("Correct!")
            score += 33.33
            print("You got 33.33 more points")
        else:
            print("The correct answer is Berlin.")

        # Question 3
        print("3. Which is the capital of France?")
        print("""a. Venice\nb. Helsinki\nc. Paris""")
        answer_3 = input("Answer:").lower().strip()
        attempts = 1
        while answer_3 not in ['c', 'paris'] and attempts < 2:
            print("Wrong. Try again.")
            answer_3 = input("Answer:").lower().strip()
            attempts += 1
        if answer_3 == "c" or answer_3 == "paris":
            print("Correct!")
            score += 33.33
            print("You got 33.33 more points")
        else:
            print("The correct answer is Paris.")
        
        print("Thanks for your time, your final score is {}, keep it hard with geography, goodbye {}.".format(score, user_name))
    else:
        print("Maybe next time!")

    # Retry Option
    retry = input("\nDo you want to retry the quiz? (yes/no): ").lower().strip()
    if retry != "yes":
        print("Goodbye!")
        break