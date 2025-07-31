import math

score_points = 0  # Tracks scoring points: 2 = full points, 1 = partial

def check_guess():
    global score_points
    for i in range(0, len(content), 2):
        print(content[i])  
        answer = input("Answer: ").strip().lower()
        
        if answer == content[i + 1].strip().lower():
            print("Correct Answer!\n")
            score_points += 2  # First attempt, full points
        else:
            print("Incorrect Answer, Try again!")
            answer = input("Answer: ").strip().lower()
            if answer == content[i + 1].strip().lower():
                print("Correct Answer!\n")
                score_points += 1  # Second attempt, partial points
            else:
                print(f"Incorrect! The correct answer is {content[i + 1]}.\n")
                # No points awarded

def scores():
    score = score_points * 5  # Each point = 5 score points
    total_questions = len(content) // 2
    correct_questions = math.ceil(score_points / 2)
    if score == total_questions * 10:  # max score
        print(f"Congratulations, {name}! You answered all {total_questions} questions correctly! Your score is {score}")
    elif score >= (total_questions * 10) / 2:
        print(f"Good Job, {name}! You answered {correct_questions} questions correctly! Your score is {score}")
    elif score >= (total_questions * 10) / 5:
        print(f"Not Bad, {name}! You answered {correct_questions} questions correctly! Your score is {score}")
    else:
        print(f"Good luck next time, {name}! You answered {correct_questions} questions correctly! Your score is {score}")
    print("THANK YOU! :)")

#MAIN
print("Welcome to the PawPoints!\nThere are a variety of 20 questions.")
print("You get 2 attempts for each question.")
print("10 points are awarded for a correct first attempt.")
print("5 points are awarded for a correct second attempt.")
print("Maximum possible score: 500 points.")
print("Rules: Use only words (no numbers or special characters). Spell everything correctly!\n")
print("LET'S GET STARTED!\n")

name = input("Enter your Name: ")

# Input validation loop for level
while True:
    try:
        level = int(input("Choose the level number to play:\n1. Easy -- 1\n2. Intermediate -- 2\n3. Difficult -- 3\n"))
        if level in (1, 2, 3):
            break
        else:
            print("Invalid level. Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid integer (1, 2, or 3).")

filename = ""

if level == 1:
    filename = "easy.txt"
elif level == 2:
    filename = "intermediate.txt"
elif level == 3:
    filename = "difficult.txt"

#file-handling --stored in the same directory only
try:
    with open(filename, "r") as questions:
        content = [line.strip() for line in questions.readlines()]
    check_guess()
    scores()
except FileNotFoundError:
    print(f"File '{filename}' not found. Make sure it exists in the same directory.")
