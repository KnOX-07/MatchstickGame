matchsticks = 21

print("Welcome to the matchstick game!")
while matchsticks > 0:
    # User's turn
    user_pick = int(input("Pick 1, 2, 3, or 4 matchsticks: "))
    
    if user_pick < 1 or user_pick > 4:
        print("Invalid choice. Try again!")
        continue
    #print(f"You picked {user_pick} matchstick(s).")
    matchsticks -= user_pick
    
    # Check if user picked the last matchstick
    if matchsticks <= 0:
        print("You picked the last matchstick. You lose!")
        break

    # Computer's turn
    computer_pick = 5 - user_pick  # Computer picks to make the total divisible by 5
    print(f"Computer picks {computer_pick}.")
    matchsticks -= computer_pick

    # Check if computer picked the last matchstick
    if matchsticks <= 0:
        print("Computer picked the last matchstick. You win!")
        break
