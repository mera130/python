import random
attempt_list = []

def showScore():
    if len(attempt_list) <= 0:
        print("there's is currently no highscore. It's ypur turn taking")
    else:
        print("current highsore is {} " .format(min(attempt_list)))
        
def startGame():
    random_number = random.randint(1, 10)
    print("greetings to our guessing")
    player_name = input("please enter your name")
    wannaPlay = input("hi,{} do you wanna play the game (yes/no)".format(player_name))
    
    attempt = 0
    showScore()
    
    while wannaPlay.lower() == "yes":
        try:
            guess = input("enter a number between 1 to 10")
            
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("please folloe the instruction")
            
            if int(guess) == random_number:
                print("congrat!! its correct")
                attempt = 0
                attempt_list.append(attempt)
                
                print("it toke you{} attempts".format(attempt))
                
                playAgain = input("do you wanna play again?(yes/no)")
                attempt = 0
                showScore()
                random_number = random.randint(1, 10)
                
                if playAgain.lower() == "no":
                    print("thats cool, have a wonderful day")
                    break
                
            elif int(guess) < random_number:
                print("opps!! the number you chose is lower")
                attempt += 1
                
            elif int(guess) > random_number:
                print("opps!! the number you chose is lower")
                attempt += 1
                
        except ValueError as err:
            print("thats not valid")
            print("{}" .format(err))
            
            
    else:
        print("thats cool, have a nice day")
        
if __name__ == '__main__':
    
    startGame()
    

                
                
                

                