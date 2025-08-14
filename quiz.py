def run_quiz():
    print("Welcome to the astronomy Quiz!")
    print("Please answer the following questions:")
    
    # Initialize score
    score = 0
    
    # Question 1
    print("\n1. What is the biggest planet in our solar system?")
    print("a) saturn")
    print("b) jupiter")
    print("c) earth")
    print("d)  the Sun")
    answer1 = input("Your answer (a/b/c/d): ").lower()
    if answer1 == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is b) Paris")
    
       # Question 2
    print("\n2. Which planet is known as the Red Planet?")
    print("a) Venus")
    print("b) Mars")
    print("c) Jupiter")
    print("d) Saturn")
    answer2 = input("Your answer (a/b/c/d): ").lower()
    if answer2 == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is b) Mars")
    
     # Question 3
    print("\n3. what is our neighboring galaxy?")
    print("a) black eye galaxy")
    print("b) condor galaxy")
    print("c) andromeda galaxy")
    print("d) milky way")
    answer3 = input("Your answer (a/b/c/d): ").lower()
    if answer3 == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is c) 12")
    
    # final score
    print(f"\n congrats!! your Quiz is completed! Your final score is: {score}/3")
    return score
    