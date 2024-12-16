import random

# Setting a random score for the user to beat
score_to_beat = random.randint(12, 17)
print(f"The score to beat is: {score_to_beat}!\n")

attempts = {}
# Giving the user 3 tries to reach/beat the score
for try_number in range (1, 4):
    print(f"Try #{try_number}:")

    # Initial roll
    dice = [random.randint(1, 6) for _ in range(3)]
    print(f"Initial roll: {dice}")

    rolls = [dice.copy()]
    reroll_count = 0

    while reroll_count < 3:
        # Check for tuple out
        if len(set(dice)) == 1:
            print("Sorry. You tupled out due to 3 same number!")
            break

        # Check is 2 dice are similar and one is not
        if len(set(dice)) == 2:
            # creating a fixed value for the two similar numbers.
            fixed_value = max(set(dice), key = dice.count)

            # non-fixed value can be changed by the user.
            non_fixed_index = dice.index(min(set(dice), key = dice.count))

            # Keep asking the user for an input until a correct response is given (y or n)
            while True:
                reroll = input(f"Two dice are fixed at {fixed_value}. Do you want to reroll the {dice[non_fixed_index]}? (y/n): ").lower()
                if (reroll == "y" or reroll == "n"):
                    break
                else:
                    print(f"\"{reroll}\" is not a valid option. Please try again!\n")

            if reroll == "y":
                dice[non_fixed_index] = random.randint(1, 6)
                rolls.append(dice.copy())
                print(f"New roll: {dice}")
                reroll_count += 1
            else:
                break
        
        # If all 3 numbers are different, re-roll all three dice.
        elif len(set(dice)) == 3:
            # Keep asking the user for an input until a correct response is given (y or n)
            while True:
                reroll = input("Do you want to reroll all dice? (y/n): ").lower()
                if (reroll == "y" or reroll == "n"):
                    break
                else:
                    print(f"\"{reroll}\" is not a valid option. Please try again!\n")
            
            if reroll == "y":
                dice = [random.randint(1, 6) for _ in range(3)]
                rolls.append(dice.copy())
                print(f"New roll: {dice}")
                reroll_count += 1
            else:
                break

        print(f"Re-rolls left: {3 - reroll_count}")

        if reroll_count == 3:
            print("No more re-rolls left.")

    # Add score only if all 3 numbers are NOT same. Else, the score should be 0.
    score = sum(dice) if len(set(dice)) > 1 else 0
    attempts[f"Try #{try_number}"] = {"rolls": rolls, "score": score}
    print(f"Score for this turn: {score}\n")

    # Customized message if the user wins...
    if score == score_to_beat:
        # If the user matches the score, say the following...
        print(f"Good Job! You matched the score of {score_to_beat}.")
        break
    elif score > score_to_beat:
        # If the user exceeds the score, display this message...
        print(f"Congratulations! You've beaten the score of {score_to_beat}.\n")
        break
    
    # This message will only print if neither of the user's score reaches/beats the score.
    if try_number == 3 and score < score_to_beat:
        print(f"Game over. You didn't beat the score of {score_to_beat} in 3 tries.\n")

#Print the attempts dictionary
print("\nAttempts Summary:\n")
for try_num, data in attempts.items():
    print(f"{try_num}:")
    print(f"Rolls: {data['rolls']}")
    print(f"Score: {data['score']}\n")